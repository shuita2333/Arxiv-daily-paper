# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 1. [Replay in the Silent Degrees of Freedom: Continual Learning Without an Offline Phase](https://arxiv.org/abs/2609.31630)

**<font color=#1a73e8>作者：</font>** Zhang Yanhai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Replay-based continual learning almost always consolidates in a dedicated offline phase or by interleaving replayed samples with the input stream, whereas brains also consolidate during wakefulness through local sleep, brief use-dependent off-periods of individual circuits. We ask whether a network trained by local, biologically constrained rules can consolidate with no offline phase at all. An isolation rule confines replay updates to hidden synapses invisible to the current input under k-winner-take-all dynamics, with optimiser state advanced only inside the mask; a refractory rotation rule makes units that have just fired sit out the next competition, widening the consolidable set; a homeostatic pressure and a relative-novelty gate decide when replay bursts fire and when rotation runs. This inverts the usual direction of non-interfering continual learning: the hidden computation on the current input is held invariant (exactly on the proven channels, and for all but 0.3% of waking samples per update elsewhere) while past memories are written into the degrees of freedom the current batch leaves unused. On class-incremental split-MNIST the system reaches 91.6+-0.3% with no offline phase, at or above the best offline-night schedule on two held-out splits, tied with DER++ and above experience replay, ER-ACE, A-GEM and unmasked local replay; in a single pass it leads DER++ (91.8% against 90.1%) while the night falls to 76.9%. The advantage is largest at small buffers and gives way to the backpropagation references at large ones; on split CIFAR-10 the system leads offline rehearsal and experience replay but trails ER-ACE and DER++. Rotation carries most of the gain; isolation adds the invariance guarantee. The mechanism is not tied to the local rule: under the same schedule a backpropagation network with k-WTA hidden layers gains from rotation, and isolation is again free on top of it.

---


### 2. [Enhancing generalization in endwall film cooling prediction: Incorporating the superposition principle into transformer-based neural operators](https://arxiv.org/abs/2609.31633)

**<font color=#1a73e8>作者：</font>** Qineng Wang, Liming Song, Tianyuan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this study, a physics-enhanced neural operator framework is proposed to enhance the generalization prediction ability of the cooling layout of a turbine endwall with variable number of film holes. Specifically, inspired by the film cooling superposition principle, we propose a film cooling prediction model, namely superposition-based deep neural operator (SDNO), that divides the endwall temperature field prediction into two stages. In the first stage, the cooling layout of a turbine endwall is divided into several sub-parts with randomly assigned film holes, and a Transformer-based neural operator network, namely Calculate Net, is designed to predict the temperature field of each sub-part. Then, in the second stage, another neural operator network, i.e., Super Net, is trained to combine the temperature fields predicted by Calculate Net for each sub-part and obtain the superposed temperature field of the full cooling layout. Additionally, instead of directly taking the film cooling contours as pixel plots, a signed distance function (SDF) which is sensitive to the variable locations of cooling holes, is designed to encode the location information of cooling holes. Furthermore, the proposed endwall film cooling prediction model is trained with the samples that changing the number of film holes from 1-5 with variable locations. Then, the trained prediction shows excellent generalization prediction ability, which can accurately predict the film effectiveness of the cooling layout with 10-20 film cooling holes that are unseen in the training samples. The proposed SDNO also improves prediction accuracy relative to the fully supervised baseline. With the above, the effectiveness of our proposed prediction model has been well demonstrated.

---


### 3. [Symmetry-quotient Flatness and Generalization](https://arxiv.org/abs/2609.31634)

**<font color=#1a73e8>作者：</font>** Taiki Miyagawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops a theorem-level pipeline in symmetry-quotient settings: quotient linear stability implies quotient flatness, quotient flatness implies input smoothness, and input smoothness yields generalization under local covering assumptions. Flatness is often associated with generalization, and Stochastic Gradient Descent (SGD) is frequently viewed as implicitly biased toward flat solutions. However, standard flatness measures are typically defined in the raw parameter space and are therefore not invariant under function-preserving symmetries such as positive rescaling. We develop a symmetry-aware theory of quotient flatness, quotient linear stability, input smoothness, and generalization on quotient spaces of neural-network parameters. For square loss and models equipped with function-preserving group actions, we define quotient flatness as the trace of the Hessian of the empirical loss on the regular quotient manifold. We show that quotient flatness controls input smoothness through a quotient-space analogue of the flatness-to-smoothness argument. We also prove that one-step mean-square quotient linear stability of the linearized SGD dynamics implies an explicit quotient-flatness bound in terms of the batch size and learning rate, and extend this analysis to higher-order tensor moments. Finally, under local covering and boundedness assumptions, we derive population generalization bounds in terms of quotient flatness and, consequently, in terms of quotient linear stability.

---


### 4. [What Next-Event Accuracy Cannot See: Closed-Loop Evaluation of Emergency Department Trajectory Simulators](https://arxiv.org/abs/2609.31635)

**<font color=#1a73e8>作者：</font>** Zhen Xuen Brandon Low  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical trajectory models are usually evaluated by next-event accuracy on observed histories. Simulation is different: models must condition on their own generated events, allowing errors to compound. Although this problem is well known in sequence modelling, it has not been systematically quantified for clinical trajectory simulators. We developed EDSim-Bench to evaluate this failure mode using 425,028 MIMIC-IV-ED stays, with external replication on MC-MED, and release the evaluation protocol and scoring code. Starting from held-out visit prefixes, models generate the remainder of each visit and are evaluated on termination, event composition, timing, conditional fidelity, and occupancy forecasting, with a train-only order-3 n-gram as a reference baseline. Despite next-event accuracies within 0.001, three neural architectures behaved very differently under rollout. Across seeds, one Transformer recipe ranged from 0.43 to 0.96 in termination score and from 4.2- to 137-fold the divergence of the n-gram; no prefix-trained neural model approached the n-gram on termination or event composition. Inference-time interventions improved termination but did not jointly recover composition and timing. Supervising every eligible sequence position rather than only the final prefix position was associated with one to two orders of magnitude lower divergence across Transformer, GRU, and LSTM models, with the pattern persisting under model scaling, temporal shift, and external-site evaluation. Nevertheless, even the best model generated visits approximately half as long as observed, and model rankings reversed on occupancy forecasting, a downstream quantity relevant to bed management. These results show that next-event accuracy is insufficient to evaluate clinical trajectory simulators and motivate closed-loop evaluation across seeds, rollout criteria, and downstream tasks.

---


### 5. [FIDAL: Diversity-Aware Federated Active Learning Under Real-World Distribution Shifts](https://arxiv.org/abs/2609.31637)

**<font color=#1a73e8>作者：</font>** David Dueñas Gaviria, Shadi Albarqouni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning enables collaborative model training across institutions without centralizing data, yet high annotation costs, domain shifts, and class imbalance remain major obstacles, especially when irrelevant out-of-distribution (OOD) samples dilute the labeled data. Existing active learning methods target uncertainty or diversity within in-distribution (ID) data and overlook unknown samples in federated clinical settings. We propose FIDAL, an open-set federated active learning framework that combines calibrated global-local evidential uncertainty, support-set diversity weighting, and adaptive OOD rejection. The rejection gate thresholds a foundation-model Gaussian-coverage signal per client and per round with Otsu's criterion, so that highly informative ID samples are queried while irrelevant outliers are excluded without any hand-tuned threshold. Evaluated on three multi-center medical imaging benchmarks (dermatology, histopathology, and mammography with organically occurring artifacts) in realistic open-set scenarios, FIDAL outperforms detector-based open-set methods by up to about 12 percentage points of balanced accuracy and is the only method on the accuracy-ID purity Pareto front of all three benchmarks. At an equal query budget it spends at least 1.3 times fewer annotations on OOD samples than every accuracy-matched baseline, saving an estimated 7-29 hours of expert reading on the mammography benchmark. By labeling only a fraction of the data pool, it matches or exceeds fully supervised performance across modalities. These results highlight the value of integrating uncertainty, diversity, and OOD rejection in open-set federated active learning for medicine.

---


### 6. [Energy-aware frugal Bayesian optimization](https://arxiv.org/abs/2609.31638)

**<font color=#1a73e8>作者：</font>** Gaston Plat, Paul Saves, Nathalie Bartoli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern design optimization frameworks aim first and foremost for models with the most accurate predictions without balancing computational overhead. It remains a reason why scaled architecture and multidisciplinary design optimization problems are difficult to address, even with sample-efficient Bayesian optimizers. In this paper, a metric quantifying the computational energy footprint is introduced within a Bayesian optimization framework to guide the parameter setting of a model towards configurations that balance both performance and frugality. The computer experiments highlighted existing tradeoffs between optimum convergence and the underlying energy footprint, and sometimes resulted in both a better-found optimum and lower energy consumption.

---


### 7. [When Does Domain Adaptation Help on Physical Vibration Sensors? A Held-Out-Bearing Study of Neural-Operator and Convolutional Models](https://arxiv.org/abs/2609.31639)

**<font color=#1a73e8>作者：</font>** Kumbha Nagaswetha, Rabi Pathak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diagnosing rolling-element bearing faults from vibration is a canonical physical-sensing task and a widely used benchmark for domain adaptation under operating-condition shift. Accuracies above 99 percent are commonly reported, but under evaluation splits that place the same physical bearing in both training and test. We revisit the task under a held-out-bearing protocol, assigning every bearing unit entirely to either the training or the test set, and find that source-only transfer is far weaker than such numbers suggest: on a change of shaft speed it reaches only $0.36$, against a target-supervised ceiling of 0.97. We then study what governs transfer. Treating computed order tracking, a shaft-angle resampling that places fault frequencies at fixed shaft orders independent of running speed, as a controlled change of representation, we find that a Fourier Neural Operator raises source-only transfer from $0.36$ to $0.61$ on the speed shift, where the fault peaks move, while a convolutional network of matched feature dimension stays near chance in both representations. The representation also decides whether unsupervised alignment can work: with the same normalized RBF-MMD loss and no target labels, the operator reaches 0.71 in the frequency domain but 0.95 in the order domain, within 0.02 of the target-supervised ceiling and above $0.86$ on every held-out bearing fold. Once the representation is right, a small label budget adds little. These results indicate that, for this task, the input representation rather than the alignment method decides whether adaptation helps. A second dataset, whose held-out units are fault diameters rather than bearings, shows that the same protocol exposes failures that even a target-supervised model cannot avoid.

---


### 8. [Product-Aware Deterministic Rounding for Quantized Matrix Multiplication](https://arxiv.org/abs/2609.31641)

**<font color=#1a73e8>作者：</font>** Piyush Sao, Narasinga Miniskar, Pedro Valero-Lara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scalar rounding decisions interact through matrix multiplication. We study deterministic
product-aware rounding after scales, clipping bounds, and grids are fixed, with each active
scalar choosing between adjacent levels. For dynamic activation rounding, null-space
reduction preserves the relaxed product while leaving at most $r$ fractional decisions, where
$r$ is the rank of the active gap-weighted weight block. Conditional-expectation completion
gives a deterministic polynomial-time algorithm with squared product error at most $
\mathrm{OPT}_{\mathrm{dyn}}+r\nu_{\max}^2/4$, where $\mathrm{OPT}_{\mathrm{dyn}}$ is the best
admissible error and $\nu_{\max}$ is the largest row norm of that block. For reusable static
weights, the exact expected product-loss metric is the uncentered input second moment with
fixed output bias; free bias recalibration yields the centered covariance. Exact optimization
is NP-hard even at rank one. In balanced blocks with $K=1024$ and $r=16$, conditional-
expectation completion attains a dither-normalized median error of $0.010$, compared with
$0.899$ for round-to-nearest. Clipping-aware initialization reduces median normalized error
by a factor of $43.4$ at ten-percent clipping. Held-out Digits experiments show that
retaining the input mean or correcting the output bias improves median product error over
round-to-nearest in all four tested bit-width and calibration-size settings.

---


### 9. [STAR: Adaptive Spatial-Temporal Normalization for Unified Microservice Incident Management](https://arxiv.org/abs/2609.31645)

**<font color=#1a73e8>作者：</font>** Xinhua Miao, Linyu Zhu, Bowei Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated incident management in large-scale microservice systems relies on learning robust representations from multimodal observability data, including metrics, logs, and traces. Although recent self-supervised frameworks enable unified modeling for anomaly detection (AD), failure triage (FT), and root cause localization (RCL), they often struggle with non-stationary temporal dynamics and heterogeneous service dependency structures. In this paper, we propose STAR, a Spatial-Temporal Adaptive Representation learning framework that explicitly addresses these challenges through adaptive normalizations. STAR introduces two tightly coupled mechanisms: Temporal Adaptive Normalization (TAN), which dynamically normalizes multivariate time series using multi-scale temporal context, and Spatial Adaptive Normalization (SAN), which performs structure-aware normalization over service dependency graphs. Unlike prior methods that treat normalization as static or task-agnostic, STAR formulates it as a learnable, context-conditioned transformation aligned with the intrinsic properties of microservice systems. The resulting adaptive representations are integrated into a unified self-supervised framework, enabling end-to-end unsupervised support for AD, FT, and RCL tasks. Extensive experiments on two real-world microservice benchmarks demonstrate that STAR consistently outperforms all state-of-the-art baselines, yielding significant and stable improvements across all three tasks. Our results highlight adaptive normalization as a principled and effective mechanism for robust multimodal representation learning in complex software systems.

---


### 10. [Typed Temporal Interaction Features for Simulation-Backed Forecasting of Open-Source Game Release Incidents](https://arxiv.org/abs/2609.31647)

**<font color=#1a73e8>作者：</font>** Shayma Alkobaisi, Anas Ali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-source video-game quality depends on inter-actions among code, assets, configuration, tests, contributors, and issue workflows, yet conventional defect predictors usually flatten or omit these relations. We investigate release-level forecasting of a quality incident within thirty days using GAMEQUALGRAPH-Pilot, a typed temporal feature pipeline with calibrated risk estimates and effort-aware ranking. Because the accessible OS-SGameBench materials do not provide manually audited release dates and outbreak labels, the executed evaluation is explicitly simulation-backed rather than an empirical claim about real games. Five seeded worlds each contain 120 projects and 24 releases, with project-disjoint validation and future cross-project testing. The pilot obtains an AUPRC of 0.520, AUROC of 0.673, Brier score of 0.207, and 29.68% effort-aware recall at a twenty-percent testing budget. Its closest local comparator, Static-Hetero-Reimpl, reaches 0.522 AUPRC; the -0.002 difference is not statistically significant after Holm correction. Inference requires 0.023 milliseconds per release in the measured environment. Ablations and controlled missingness, drift, engine, project-size, alert-threshold, and attribution analyses expose where typed interactions help and where they fail. Results support the reproducibility of the proposed protocol, not deployment effectiveness. Real OSSGameBench release reconstruction, stratified label audits, and official graph-model comparisons remain mandatory before journal submission or operational use in practice. This boundary protects research integrity and supports credible evaluation.

---


### 11. [A literature-guided descriptor-based framework for filtering composition search spaces](https://arxiv.org/abs/2609.31650)

**<font color=#1a73e8>作者：</font>** Lei Zhang, Markus Stricker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific literature contains latent knowledge about materials behavior, but much of this knowledge is expressed through words, contexts, and recurring associations rather than explicit design principles. This raises a central question: how can large-scale scientific corpora be used for practical problems in materials discovery? Here, we present a literature-guided descriptor-based filtering framework for reducing composition search spaces. For a given performance metric, the framework selects two descriptors from a filtered vocabulary in a literature-trained word embedding model and uses the selected descriptors to construct a Pareto-based filter for candidate compositions. Across the evaluated performance metrics and composition search spaces, the framework filters out an average of 74.27\% of the candidate compositions, with an average best-value error of 1.93\% relative to experimental measurements. Compared with expert-chosen and random descriptors, our performance metric-dependent descriptors provide a more controlled balance between retained fraction and best-value error. These results show that literature-derived embeddings can support intuitive and reproducible filters for narrowing candidate composition spaces while preserving high-performing compositions.

---


### 12. [Distributional sentiment modeling and anomaly detection for consumer complaint assessment](https://arxiv.org/abs/2609.31653)

**<font color=#1a73e8>作者：</font>** Peiheng Gao, Chen Yang, Shimin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentiment analysis is a common tool for converting unstructured text into quantitative signals in finance and risk management. Yet most applications reduce the output to a discrete polarity label or a single predictive feature, overlooking the distributional structure of sentiment intensity in consumer complaint narratives. In this paper we treat negative sentiment in consumer complaints as a bounded continuous variable and study its full distribution rather than a single label. We score each narrative with a transformer classifier, model the scores with Beta distributions, and compare the fitted distributions of meritorious and non-meritorious complaints through the Kullback Leibler divergence and the squared Hellinger distance. The fitted distributions are then linked with dollar amounts and company response outcomes to construct anomaly diagnostics that flag complaints whose textual severity is inconsistent with the recorded relief. We find that the two groups have strongly overlapping distributions, so negative sentiment intensity is not a sharp classifier of outcomes on its own; combined with monetary and categorical attributes, it isolates unusually severe complaints for operational risk monitoring. Treating sentiment analysis as continuous distributional measurement, this study links sentiment extraction, bounded response modeling, and anomaly detection in a unified framework for consumer complaint assessment.

---


### 13. [Temporal-Attention Head Specialization During Video Diffusion Training](https://arxiv.org/abs/2609.31654)

**<font color=#1a73e8>作者：</font>** Taewoo Ha, Shafayat Mowla Anik, Dae Yeol Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers depend on temporal attention to coordinate information across frames, yet nearly everything known about this mechanism comes from analyzing trained models, so when and where temporal-attention structure forms during training remains poorly characterized. Population averages can also hide it, since a few specializing heads and a diffusing majority cancel in the mean. We therefore conduct a checkpoint-resolved census of every temporal-attention head across nine Open-Sora STDiT training runs spanning three model scales (306M to 1.03B parameters), scoring each head with an entropy-normalized measure of cross-frame attention concentration (CFAC) under a preregistered change-point and effect-size selection rule. The census reveals the sparse picture that averages obscure. Aggregate CFAC is flat or decreasing in every run, while a small minority of heads, roughly 4--13% in full-grid runs, develops pronounced concentration. Across seeds, the reproducible signal is positional but block-level. Selected heads repeatedly arise in the first temporal block, whereas individual head coordinates do not reproduce once block membership is accounted for. Among the analyzed 760M selected heads, attention maps converge to a small repertoire of local frame-routing motifs, self-frame diagonals and adjacent-frame bands, even when the responsible coordinates differ across runs. Correlation and ablation analyses do not establish a causal link to generated video quality, and we bound our claims accordingly. Beyond this STDiT family, the study contributes a transferable methodology. Checkpoint-resolved, per-head analysis under fixed selection rules can expose sparse temporal organization in other factorized video diffusion transformers and, with adapted routing metrics, in joint spatio-temporal architectures.

---


### 14. [One Evaluation, Any Operating Point: Hypernetwork-Amortized MeanFlow for 3D MRI Reconstruction](https://arxiv.org/abs/2609.31655)

**<font color=#1a73e8>作者：</font>** Ruibo Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative priors reconstruct accelerated 3D MRI well but pay heavily at deployment: tens of network evaluations per volume, and protocol-specific hyperparameter tuning. A third hidden cost is the scanner's fixed sampling pattern. We treat the whole operating point as an input. A 3D MeanFlow patch network (a one-step flow model) is fine-tuned end-to-end through a warm-started, five-iteration differentiable conjugate-gradient projection. A small hypernetwork maps the operating point (data-consistency weight, acceleration, and the Cartesian sampling pattern itself) to the network's per-channel modulation. Three findings follow. (i) Learning the acquisition is worth more than any other operating point: on clinical knee data, the learned mask gains up to +2.34 dB over the protocol's variable-density mask. This gain requires the solver: with a feed-forward reconstructor the same learned mask hurts at 4x (-1.7 dB), but with the data-consistency projection it adds +4.6 dB. (ii) One evaluation is highly effective: it beats a 20-step patch-diffusion prior by up to +3.1 dB on brain and +2.9 dB on knee. Three to five evaluations extend the front to +6 dB while using a quarter of the prior's network calls. (iii) Fully sampled targets are optional: trained self-supervised on a split of acquired samples, the reconstructor matches its supervised twin at 4x on real data. Finally, we report what failed and why: subject-adaptive acquisition from measured energy, combining self-supervision with learned acquisition, and amortising the data-consistency weight.

---


### 15. [From Phase Transition to Systemic Failure: A Decoupled Analytics Framework for GNN Robustness](https://arxiv.org/abs/2609.31656)

**<font color=#1a73e8>作者：</font>** Shuai Yan, Dan Peng, Jie Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data quality is a major bottleneck for the reliable deployment of graph neural networks (GNNs) in real-world graph mining tasks. Among various sources of degradation, label noise and feature distribution shift (hereafter referred to as distribution shift) are two common yet fundamentally different challenges. To study their effects under controlled conditions, this paper constructs a synthetic homophilic graph regression benchmark in which the two factors can be manipulated separately. A total of 41 configurations and 410 runs are conducted to evaluate the behavior of representative GNN models under varying noise and shift conditions. The results show two distinct patterns. First, under additive label corruption, performance remains relatively stable over a broad range of noise settings and begins to deteriorate sharply only after an observed transition region around the 50 percent noise ratio. Second, under extreme feature distribution shift, all tested models suffer substantial degradation, with test MSE increasing by 48 times to 316 times and correlation dropping by 73 percent to 89 percent. These findings suggest that, in the present controlled setting, GNNs are considerably more tolerant to moderate label perturbation than to severe distribution mismatch. The study provides a controlled empirical baseline for understanding how data quality affects GNN-based graph mining systems and offers practical implications for deployment-oriented monitoring and model maintenance.

---


### 16. [Cross-Dataset Transfer and Unknown-Class Detection in Imbalanced SAR Ship Classification](https://arxiv.org/abs/2609.31658)

**<font color=#1a73e8>作者：</font>** Ch Muhammad Awais, Marco Reggiannini, Davide Moroni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ship classification from Synthetic Aperture Radar (SAR) imagery is a critical computer vision task, yet the robustness of models under deployment shifts remains unclear. While models are often trained on one dataset and deployed on another, we lack a comprehensive understanding of their cross-dataset generalization. To address this, we evaluate six pretrained models on two SAR ship datasets in three settings: in-domain classification, cross-dataset transfer, and unknown-class detection. For unknown detection, we hold out all classes one at a time. In-domain, SARDet100K gives the best balanced accuracy on both datasets (73.4\% on FUSARShip and 53.2\% on OpenSARShip). In cross-dataset transfer, we observe strong failures: some models show moderate accuracy but near-chance balanced accuracy (for example, 64.5\% accuracy but 33.3\% balanced accuracy for OpenSARShip to FUSARShip). In unknown detection, performance depends on the held-out class and dataset, while MC-dropout variance is often close to random. These findings show that cross-dataset generalization in SAR remains limited and that task-specific uncertainty scores are often more informative than MC-dropout variance for held-out-class detection, although their relative ranking depends on the dataset and held-out class.

---


### 17. [Cross-Material Support Transfer for Core-Loss Prediction Under Waveform Covariate Shift](https://arxiv.org/abs/2609.31659)

**<font color=#1a73e8>作者：</font>** Cong Yao, Chunye Gong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Power magnetic materials are characterized on the sinusoidal and triangular waveforms that excitation hardware conveniently produces, whereas deployed converters expose cores to trapezoidal, PWM-shaped flux trajectories, so loss models must predict exactly where their training data are thinnest. The final test of the MagNet Challenge embeds a deliberately extreme instance of this characterization-deployment mismatch: for material D, trapezoids form 16.4% of the test set but only 1.4% of the training set. The 95th-percentile relative error, hereafter p95, of the best submission, built on sequential transfer learning, stalled at 15.9%, the worst among the five materials. This paper shows that the obstacle is missing information under covariate shift rather than class imbalance, and that the missing support can be borrowed from sibling materials instead of being extrapolated. Controlled experiments first refute the imbalance reading: four standard remedies fail, and raising the trapezoidal share to the test-set level degrades accuracy further. The proposed material-identity support transfer, MIST, then trains one 2784-parameter predictor jointly on all five challenge materials. Material identity enters through feature-wise linear modulation, or FiLM, the scarce material's true-label loss is reweighted, and material D receives no fine-tuning, so that the bias of its trapezoid-free training set is never re-installed. MIST lowers the five-seed material-D p95 from 20.39+/-2.03% to 12.38+/-0.92% and the trapezoidal-class p95 from 37.4+/-8.8% to 15.16+/-1.69%, surpassing the best submission with one-sixth of its parameters and no fine-tuning stage; removing material identity at matched capacity inflates the error by an order of magnitude. These results argue that scarce materials should be characterized jointly with their siblings.

---


### 18. [Learning Steadily: Accumulating Relative Point Margin Scores for Face Image Quality Assessment](https://arxiv.org/abs/2609.31662)

**<font color=#1a73e8>作者：</font>** Guray Ozgur, Tahar Chettaoui, Eduarda Caldeira 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Image Quality Assessment determines the suitability of captured face images for automated face recognition (FR), a critical capability for reliable biometric systems. Existing state-of-the-art FR-integrated FIQA methods suffer from temporal instability: as the feature space evolves during training, single-epoch quality estimates fluctuate, creating a moving target that undermines reliable quality prediction. We introduce CARPM-FIQA, a stabilization strategy for FR-integrated FIQA that accumulates relative point margin measurements, the ratio between intra-class compactness and inter-class separation, across the entire training trajectory rather than relying on single-epoch estimates. This cumulative averaging approach provides theoretically grounded advantages: reduced variance in quality estimates, improved mean squared error, and enhanced ranking stability with convergence guarantees as training progresses. Through controlled experiments on the SynFIQA dataset with labeled quality groups, we demonstrate that cumulative averaging achieves superior discriminative ability, and ablation studies across different training configurations confirm consistent improvements. Evaluated against twelve FIQA methods on eight challenging benchmarks with four FR models at two FMR thresholds, CARPM-FIQA places 4th (CARPM-FIQA(L)) and 6th (CARPM-FIQA(S)) of 17 compared methods by pAUC-EDC and AUC-EDC averaged across FR models and, after per-benchmark normalization, across benchmarks, staying within a few percent of the best method's normalized average for every FR model, providing a principled solution to training instability while maintaining the performance benefits of FR integration. More broadly, our work demonstrates that temporal aggregation strategies can stabilize training objectives in deep learning systems where target values inherently fluctuate due to evolving feature representations.

---


### 19. [Age-Adaptive Handwriting Reconstruction from an IMU-Based Digital Pen through Shared Representations and Domain-Specific Heads](https://arxiv.org/abs/2609.31666)

**<font color=#1a73e8>作者：</font>** Florent Imbert, Yann Soullard, Eric Anquetil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Digital pens are widely used to capture handwriting on digital devices, enabling precise trace recording and enhancing human-computer interaction. However, most are bundled with tablets and lack cross-brand compatibility. Recent digital pens equipped with kinematic sensors have emerged, designed for use on any surface. This especially opens significant potential for supporting handwriting acquisition in classrooms.  Handwriting reconstruction from such an IMU-equipped pen poses a challenge due to the significant variability in sensor signals between adults and children. Even when producing visually similar traces, variations in writing dynamics, motor control, pen holding, and user confidence introduce substantial discrepancies in the captured signals. Additionally, the high variability in children's handwriting requires collecting large amounts of data, which is not feasible to implement in a school environment at scale. Furthermore, models trained exclusively on adult data fail to generalize to children's handwriting, and conversely, models trained on children's data perform poorly on adult writers. This crosspopulation degradation highlights the need for a unified model that can be deployed directly on the pen, without any user-specific adaptation. To address this issue, we propose a cross-domain learning, using an original neural network architecture based on a Temporal Convolutional Network and multiple prediction heads. The model is designed to be robust across age groups by leveraging shared features while effectively handling variability induced by differences in graphomotor development. This approach aims to improve handwriting trace reconstruction from sensor data, where each domain benefits from additional data provided by the other domain.

---


### 20. [Beyond the Graph: An Adaptive Meta-Learner Fuses Explainability, Weather, and Dynamics for Robust Bus ETA Prediction](https://arxiv.org/abs/2609.31667)

**<font color=#1a73e8>作者：</font>** Pratham Payra, Jagadish  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate bus Estimated Time of Arrival (ETA) prediction is vital for urban mobility, passenger satisfaction, and transit efficiency, yet existing models falter against nonlinear spatiotemporal dynamics, data sparsity, and factors such as weather. This paper proposes HYB(nm), an adaptive hybrid ensemble framework that dynamically fuses five complementary models - a historical baseline (MST-AV), periodical temporal pattern analysis (GDRN-DFT), Koopman Neural Operators for nonlinear dynamics (KOOP-NET), weather-integrated feature-engineered neural networks (FENN), and real-time graph convolutional networks (MGCN) - via a meta-learner attuned to real-time context. Evaluated on GPS and weather data from three Kolkata bus routes comprising more than 4,000 trips, the framework leverages the individual strengths of its components (for example, the low-latency explainability of MST-AV, the weather resilience of FENN, and the network-dynamics capture of MGCN) to deliver the superior robustness of HYB(2), state-of-the-art accuracy rivalling leading graph neural networks, and balanced trade-offs in stability and efficiency across prediction horizons and operating conditions. The extensible HYB(k) architecture equips transit agencies with flexible tools, ranging from economical single models to tailored high-fidelity hybrids, advancing predictive, equitable urban transport.

---


### 21. [NanoForecast v0.5: Competitive Time Series Forecasting Through Training Pipeline Optimization](https://arxiv.org/abs/2609.31669)

**<font color=#1a73e8>作者：</font>** Gautam Kishore  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present NanoForecast v0.5, a 6.5M-parameter forecaster that competes with models 31x its size (TimesFM, 200M parameters) after training pipeline fixes and no architecture change. Retraining the v0.3 architecture with corrected loss-scope handling, tensor shape alignment, and wider augmentation coverage cuts overall Mean Absolute Scaled Error by 43.8% under one fixed protocol (MASE 3.030 to 1.704) on the same data and compute budget. NanoForecast v0.5 beats TimesFM on all three ETT datasets (MASE 0.676/1.110/0.287 vs. 0.705/1.360/0.545) and on exchange rate (4.317 vs. 4.383); TimesFM keeps a clear lead on the high-cardinality electricity and traffic sets. Against PatchTST (15M+ parameters, official configuration), v0.5 wins all three ETT sets. Training takes about 12 hours on a single cloud GPU (NVIDIA T4, Google Colab) and inference needs no GPU (measurements in this paper are on an Apple M4 CPU). We release all code, pretrained checkpoints, and evaluation framework under Apache 2.0 at this https URL

---


### 22. [One-Step Is Optimal: Unconditional Rectified Flows are Noise2Noise Denoisers, and Multi-Step Integration Provably Hurts---A Benchmark and Task-Based Detectability Study on Low-Dose CT](https://arxiv.org/abs/2609.31670)

**<font color=#1a73e8>作者：</font>** Timothy Sereda, Debesh Jha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iterative and generative denoisers are increasingly used under the assumption that multi-step refinement outperforms a single regression pass. We show the opposite for \emph{label-free} denoising. An \emph{unconditional} rectified flow trained on two noisy observations of the same signal, as in Noise2Noise, has a minimiser whose one-step readout is exactly the MMSE denoiser without requiring clean targets. In contrast, multi-step integration provably departs from the MMSE solution because the flow terminates at the noisy data distribution rather than the clean-signal distribution. This departure is exact in a tractable Gaussian model and is confirmed experimentally: one-step flow matches a direct regressor, whereas multi-step Euler integration progressively reduces fidelity. Counterintuitively, the degradation increases with training quality, as a better velocity field more faithfully transports samples toward the noisy terminal law. The key ingredient is therefore the decorrelated \emph{pairing}, not the flow machinery: a one-step regressor trained on matched noisy pairs gives our best label-free result ($+1.99$,dB). We evaluate these findings on \textbf{CTDenoiser}, a controlled low-dose CT benchmark spanning five architectures and supervised, similarity-based, blind-spot, and per-image methods. Among label-free approaches, only correlated-noise-aware Noise2Sim improves over the noisy baseline, while Noise2Void is flat-to-negative because CT noise violates its pixel-independence assumption. Finally, although supervised denoisers gain approximately $4$,dB PSNR, a channelized Hotelling observer shows reduced low-contrast lesion detectability, revealing clinically relevant degradation missed by PSNR and SSIM.

---


### 23. [Unsupervised spiking feature learning for event-based pedestrian crossing detection: approaching supervised accuracy without labelled training data](https://arxiv.org/abs/2609.31671)

**<font color=#1a73e8>作者：</font>** Henok Teklu, Mustafa Sakhai, Matej Mertik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras are well suited to pedestrian crossing detection, and spiking neural networks (SNNs) can process their output natively, but current SNN detectors are trained with supervised backpropagation and therefore require costly frame-level crossing labels. We investigate crossing detection with no labels in feature learning and report the first unsupervised results on the recent DVS-PedX pedestrian-crossing benchmark. A single spiking layer trained with winner-take-all spike-timing-dependent plasticity learns a dictionary from unlabelled event-frame patches; frames are encoded by cosine similarity to the learned filters with spatial pooling and read out by a linear classifier, the only supervised component. On the 24,454-frame test split the method attains 90.3% accuracy and an area under the receiver operating characteristic curve (AUROC) of 0.936, compared with 92.0% and 0.943 for a supervised spiking network trained end-to-end on the same frames; under adverse weather the AUROC is 0.913. The result is insensitive to the choice of plasticity rule but depends strongly on the readout protocol: with the classical neuron-assignment readout the same network attains only 0.70 AUROC. On the benchmark's real converted portion, a readout refit lifts performance from chance (0.53) to 0.67 AUROC, within the published supervised range. These findings indicate that the accuracy cost of removing labels from feature learning is small on this benchmark, and that reported weaknesses of unsupervised spiking networks may be attributable to the readout protocol rather than to the learning rule.

---


### 24. [An Evaluation of AI-Supported Evidence-Based Learning for Public Speaking Skill Development](https://arxiv.org/abs/2609.31676)

**<font color=#1a73e8>作者：</font>** Sashini Hettiarachchi, Shahbaz Siddeeq, Mika Saari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Public speaking is an essential skill in academic and professional contexts, but it often causes anxiety. Although several AI-based speech coaching tools exist, they typically provide generic feedback and lack model speeches for learning. This study addresses these gaps by developing a system that incorporates speech context into evaluation criteria, enabling more tailored feedback. It also generates improved model speeches in both text and audio formats to support example-based learning. The system was evaluated in a pilot study with seven undergraduate students over one to three weeks. Participants used the system repeatedly and practiced the same speech at least three times. Results showed improvements in public speaking performance for all participants. Filler word usage decreased, and anxiety levels dropped by 15.3% to 34.4%. Participants found the context-aware feedback and revised speeches useful and confidence-building. These findings suggest that context-aware feedback and model speeches can enhance public speaking skills and reduce anxiety. Future studies could explore video-based analysis of physical behavior during speeches.

---


### 25. [A Comparative Transfer-Learning Study of CNN Backbones for Partial Face Recognition on the SoF Dataset](https://arxiv.org/abs/2609.31677)

**<font color=#1a73e8>作者：</font>** Ahmed Kubba, Ali Alsalama, Abdelrahman Abdalla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition is widely deployed in surveillance, access control, and forensic workflows, yet accuracy degrades sharply once the face is occluded by accessories, foreground objects, or the frame edge. Because most faces in the wild are partial, robust partial face recognition (PFR) remains open. This paper compares three pretrained convolutional backbones, ResNet-50, VGG-16, and FaceNet, fine-tuned for PFR by transfer learning under identical preprocessing, splitting, and optimization protocols on the Specs-on-Faces (SoF) dataset. All three arms use a common 160x160 input and a frozen backbone with a trainable head under a fixed epoch budget and no per-backbone hyperparameter search. The FaceNet configuration, denoted PFN (Partial FaceNet), substantially outperforms the other two, reaching 97.4% test accuracy with macro-averaged 87.04% precision, 84.61% recall, and 84.17% F1 over the 112 identity classes, the highest accuracy and recall reported on SoF.

---


### 26. [Does Joint-Embedding Predictive Architecture Pretraining Help Time Series Forecasting?](https://arxiv.org/abs/2609.31680)

**<font color=#1a73e8>作者：</font>** Yutong Feng, Bowen Liao, See Kiong Ng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures (JEPA) have emerged as a promising self-supervised pretraining paradigm for time series, learning representations by predicting target embeddings in latent space rather than reconstructing raw signals. Yet evidence on their benefits remains mixed, and most studies test only a single backbone or a narrow set of architectures, leaving unclear whether JEPA pretraining is a reliable improvement or one that depends heavily on the downstream model. We address this gap through a large scale evaluation of one JEPA instantiation across nine backbones and eleven benchmarks spanning temporal and spatio-temporal forecasting, the most extensive cross architecture assessment of JEPA for time series to date. We find that the benefit of this instantiation varies sharply across backbones, producing consistent gains for some architectures and consistent degradation for others, even on the same dataset. This pattern holds across both task families, indicating the variability is a general property of this instantiation rather than a dataset specific artifact worth accounting for when choosing a backbone in practice.

---


### 27. [Devanagari Handwritten Character Recognition Using TrOCR: A Transformer-Based Model with Real-Time Web Deployment](https://arxiv.org/abs/2609.31681)

**<font color=#1a73e8>作者：</font>** Amrit Baskota, Samyam Budhathoki, Shubham Ghimire 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Devnagari is a one of the ancient language of the Indian subcontinent consisting of 36 vowels, 14 consonants and 10 numerals. The accurate recognition of handwritten Devnagari characters is challenging due to high complexity of Devnagari scripts. This paper presents a method to fine tune the pre trained TrOCR model to accurately recognize Devanagari handwritten characters. The Methodology consists of a preprocessing mechanism where input images are standardized into RGB format, tokenized in batches and integrated with Hugging Face Dataset. The pre-trained microsoft/trocr-base-handwritten model is fine-tuned over a dataset of nearly 5000 character images that are uniformly partitioned in the ratio 8:1:1 for training, evaluation and testing. Further optimization is done is the training process through mixed precision training, gradient checkpointing, and early stopping mechanism. The model achieves a character error rate (CER) of 3.95% and a character-level accuracy of 96.05%, outperforming the previous CNN based models. A scalable web application is developed using this http URL, Golang, and FastAPI which practically deploys the OCR model and serves character recognition task with a latency less than 5 seconds per request. This study demonstrates the use of TrOCR model to build a scalable handwritten Devnagari character recognition system and also a foundation to future research on Devnagari Script Recognition using Transformers.

---


### 28. [Towards Transparent Diagnostics: Investigating Architectural Trade-offs and Explainability in Malaria Detection](https://arxiv.org/abs/2609.31682)

**<font color=#1a73e8>作者：</font>** Suman Kunwar, Avishek Dangol  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> More than 80 countries have reported malaria cases with 610 thousand deaths and are projected to increase. Identifying malaria early and accurately helps save lives. The effective way to diagnose malaria is through microscopic methods that are labor intensive and require experts with special equipment. Deep learning (DL) has shown promising results in medical diagnosis. Here, we explored various DL models: ResNet18, MobileNetV2, EfficientNet-B2, VGG19 and also proposed a model for detecting malaria presence using blood smears taken from the NIH Malaria dataset. Our experiment shows that MobileNetV2 achieved 96.35% accuracy with the smallest model size (8.49 MB) and fastest inference (1.35 ms). The proposed model achieved 97.67% accuracy, 0.9756 AUC with longest inference time (13.17 ms). The larger architecture outputs a larger model size with moderate accuracy. Upon further pruning, the proposed model gained a slight improvement in accuracy and inference time. The GRAD-CAM, SHAP and LIME shade explainable AI (XAI) insights of the model.

---


### 29. [3-D Emissions Mapping and Social Cost Estimation for US Domestic Aviation at West Coast Hubs](https://arxiv.org/abs/2609.31686)

**<font color=#1a73e8>作者：</font>** Hesam Shafiei Nia, Don MacKenzie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing aviation emissions inventories lack accurate trajectory data for high-resolution social cost and health impact assessment. This paper develops a 3-D emissions map by reconstructing flight trajectories for US west coast hubs to estimate regional environmental and near-airport health impacts. A physics-informed autoencoder (AE) is applied to ADS-B trajectory records for January 2025 covering US west coast hubs. The encoder combines a Convolutional Neural Network (CNN), a Bi-GRU, and a 3-D CNN with skip connection; the decoder is a Temporal Convolutional Network (TCN). It is benchmarked against a baseline-AE and cubic spline interpolation. Emissions are mapped via EUROCONTROL Base of Aircraft Data (BADA) performance tables and ICAO Engine Emissions Databank (EEDB) emission indices, with altitude corrections via Boeing Fuel Flow Method 2 (BFFM2). Social costs are quantified for all flight phases, with health impacts assessed for Landing and Takeoff cycles within 50 km of each hub. The proposed AE model outperforms both a TCN-AE and cubic spline interpolation across 5% to 50% missing rates. Monetizing the emissions inventory shows NOx produces a small net cooling effect in direct climate forcing, while accounting for 99.7% of monetized air-quality and health cost despite being under 0.4% of CO2 by mass, making it the dominant health-cost driver. To our knowledge, this is among the first studies combining AE-based trajectory reconstruction with separate spatial-temporal feature encoding and altitude-based emissions modeling to produce a regional aviation emissions inventory for air quality, climate impact and population exposure. The resulting emissions map and social cost estimates provide quantitative context for environmental impact assessment and near-airport health policy evaluation for US domestic aviation.

---


### 30. [Architecture-aware Robustness Evaluation of Explainable Deep Learning for Breast Cancer Diagnosis](https://arxiv.org/abs/2609.31692)

**<font color=#1a73e8>作者：</font>** Balenthira Thanusanth, Selvarajah Thuseethan, Roshan G. Ragel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explainable Artificial Intelligence (XAI) has become essential in medical image analysis to ensure transparency of deep learning (DL)-based diagnostic systems. However, selecting appropriate XAI techniques for breast cancer recognition remains largely ad hoc, with limited systematic evaluation across different DL architectures. This study presents a systematic architecture-aware evaluation protocol to assess the effectiveness of nine widely used XAI techniques across four categories of DL models: very deep, lightweight, transformer-based and hybrid neural networks. The evaluation is conducted on a breast ultrasound dataset comprising 780 images using clinically aligned spatial metrics, including Pointing Game, Intersection over Union and Mean Coverage, to quantify agreement between generated explanations and expert-annotated lesion regions. Results indicate that explanation quality is primarily influenced by the interaction between model architecture and XAI method, rather than any single technique consistently outperforming others. Hybrid architectures produce more spatially coherent explanations, while lightweight and transformer-based models exhibit greater variability across methods. The findings show that no single technique generalises across architectures and evaluation criteria, emphasising the need for joint selection of DL models and XAI techniques. Explainability depends on both model design and explanation strategy and should not be considered independently. This work provides a structured evaluation protocol and practical guidance for selecting XAI techniques in breast cancer diagnosis, supporting more transparent clinical decision-support systems. \textcolor{blue}{Code is publicly available at this https URL}

---


### 31. [Disentangle and Drop: Robust Universal Removal of Image Watermarks via Reconstructive Grayscale Residual Decomposition](https://arxiv.org/abs/2609.31693)

**<font color=#1a73e8>作者：</font>** Qi Li, Jidong Yang, Feng-Lei Fan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Invisible image watermarks are commonly evaluated against benign postprocessing operations such as compression, resizing, blur, and color changes. These tests leave out a different threat: a learned remover that preserves semantic image content while discarding residual evidence that carries the payload. We propose Disentangle and Drop (DnD), an attack that is agnostic to the watermark method and treats watermark removal as a representation routing problem. DnD decomposes a watermarked image into a semantic grayscale carrier and an auxiliary residual branch, and then suppresses the residual branch to reduce watermark evidence. The model is trained with latent spectral perturbations and low-strength diffusion exposure so that the drop operation remains stable under adaptive reconstruction. Experiments on seven representative watermark families show that one shared operating setting gives competitive removal with high visual fidelity. Operating scans and ablations separate usable attacks from image-damaging settings: stronger noise or diffusion can raise removal scores by damaging the image, while the practical regime comes from dropping the residual latent. These results argue for evaluating watermark robustness against learned removal at the representation level, not only against conventional image edits.

---


### 32. [RemTraceNet: Few-Shot Forensic Detection of Invisible Watermark Attacks](https://arxiv.org/abs/2609.31694)

**<font color=#1a73e8>作者：</font>** Jidong Yang, Huaike Yu, Qi Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Removing an invisible watermark and concealing the forensic evidence are distinct objectives: successfully disrupting the embedded watermark does not imply that the removal process is forensically undetectable. When verification fails, removal traces can provide complementary evidence for provenance and ownership verification, whereas their absence leaves the cause of the failure ambiguous. Existing methods are typically evaluated by watermark suppression and perceptual quality, while forensic stealth is rarely considered. We therefore study watermark-attack-specific few-shot forensics: for each known pipeline, a specialist can separate its outputs from paired clean and unattacked watermarked controls. Separate Attack-vs-Clean and Attack-vs-Watermarked evaluations prevent watermark-presence shortcuts. Image-aligned and prompt-matched controls are used for post-hoc and generator-integrated schemes, respectively. In this work, we introduce RemTraceNet, which fuses constrained residuals, local relations, FFT/Haar statistics, and block-DCT evidence at native resolution. Across 23 removal pipelines and 10 watermark configurations, we evaluate native 256 x 256 and 512 x 512 inputs. With 100 attacked training images per pipeline, the three-seed TPR@1%FPR, macro-averaged over attacks and watermark configurations, ranges from 82.75% to 88.17% across resolutions and control types. Under the condition of same labels and protocol, RemTraceNet outperforms retrained SRNet, ZhuNet, and SiaStegNet baselines by 10.80--15.68 percentage points. Extensive experimental results show that erasing a watermark and erasing evidence of its removal are distinct challenges, and that removal traces remain learnable under limited supervision.

---


### 33. [RPA: Residual Patch-Token Adapter for Image Retrieval from EEG and MEG](https://arxiv.org/abs/2609.31698)

**<font color=#1a73e8>作者：</font>** Yuhui Jin, Yonghao Song, Bingchuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing MEG and EEG (M/EEG) visual decoding methods align brain signals with a single global embedding extracted from a pretrained visual encoder, leaving open whether intermediate patch representations, which preserve richer and more granular rich visual information, can improve representation learning. To address this question, we introduce the Residual Patch Adapter (RPA), a lightweight, modular adapter that leverages all patch tokens from an intermediate layer of a ViT visual encoder for alignment. Through extensive ablation analyses, we first show that pooling or masking patch tokens degrades the learned representation, demonstrating that retaining the full set of patch tokens is important for EEG alignment, while the CLS token provides little unique information. We then use a series of six quantitative feature analyses to show that both higher-level semantics and lower-level visual features, including color and texture, are essential for this EEG-to-image alignment. Under current protocols, our system achieves Top-1 accuracies of 95.4\% within-subject and 35.5\% cross-subject on THINGS-EEG2, and 65.2\% and 6.7\%, respectively, on THINGS-MEG, achieving state-of-the-art (SOTA) performance across both datasets. Evaluations with alternative brain encoders, including pretrained EEG foundation models, demonstrate that the approach extends beyond the projection-based EEG encoder. Furthermore, we provide a plug-and-play interface that allows RPA to be replaced by convolution, attention, or ConvNeXt alternatives. Together, these findings provide significant insight into M/EEG-to-image representation learning by establishing design principles for leveraging the latent space of visual encoders, and open new directions for brain--image alignment and non-invasive brain--computer interface (BCI).

---


### 34. [Integrated Deep Learning Framework Designed on Hybrid Optimization Strategies for Automated Health Detection and Analysis in Silkworms](https://arxiv.org/abs/2609.31701)

**<font color=#1a73e8>作者：</font>** Komala K V, Lata B T, Venugopal K R  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A Hybrid Residual Attention Network is proposed for accurately classifying silkworm images into six different classes, including healthy and diseased states. It uses residual blocks for deep feature extraction and attention to focus on disease related features. A novel Integrated Adaptive Momentum Optimizer was introduced to enhance convergence and improve training efficiency. The dataset of silkworm images underwent preprocessing techniques such as normalization, resizing, and noise reduction, along with augmentation strategies to improve data quality and diversity. It is optimized using IAMO, achieved an accuracy of 98.67%.The integration of spatial and channel wise attention mechanisms, coupled with IAMO, significantly enhanced the model ability to recognize subtle differences between classes. Results indicate that HRAN can be used to detect disease at an early stage in sericulture, and future work will enhance scalability and efficiency in different environments.

---


### 35. [CLC-YOLO: A Compact Channel-Gated Prototype Network for Real-Time Leakage-Aware Breast Ultrasound Lesion Segmentation](https://arxiv.org/abs/2609.31702)

**<font color=#1a73e8>作者：</font>** M. Fazri Nizar, Muhammad Naufal Rachmatullah, Julian Supardi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable breast ultrasound lesion segmentation requires accurate boundaries and evaluation that prevents patients or duplicate images from crossing data splits. We propose Channel Local Contrast (CLC), a compact refinement of the YOLO26 segmentation prototype head. CLC adds a fixed local high-pass residual controlled by 64 zero-initialized, bounded channel gates. Baseline and CLC were compared in five matched folds on each of four breast ultrasound datasets. BUS-BRA used patient-disjoint outer tests with separate inner validation. BUS-UCLM and BrEaST used patient-grouped validation folds; BUSI used duplicate-component groups because patient identifiers are unavailable. Group-macro Dice increased by 1.68, 3.11, 1.12, and 2.45 percentage points on BUS-BRA, BUS-UCLM, BUSI, and BrEaST, respectively. Only the BUS-BRA paired 95% confidence interval excluded zero. CLC adds 64 parameters and 0.0049 giga floating-point operations (GFLOPs). At 640 pixels, single-T4, batch-one, 16-bit floating-point (FP16) TensorRT graph times were 2.1478 ms for CLC and 2.0512 ms for baseline, excluding preprocessing and postprocessing. CLC increased group-macro Dice across all four datasets with a measured T4 forward-pass overhead of 0.0966 ms. Code: this https URL

---


### 36. [Cross-Dataset Generalization of Bangladeshi Rice Leaf Disease Classifiers: Benchmark, Diagnosis, and Mitigation](https://arxiv.org/abs/2609.31709)

**<font color=#1a73e8>作者：</font>** Anindya Paul  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-dataset transfer in rice leaf disease classification remains a significant challenge, with models trained on one image collection performing substantially worse when deployed on another. We conduct a systematic benchmark across three Bangladeshi rice leaf disease datasets (5,419 images, 6 transfer pairs, 3 CNN backbones, 3 random seeds) to characterize and diagnose this failure. Strong augmentation recovers a mean cross-dataset macro-F1 improvement of +0.070 (Wilcoxon p < 0.001, 15 of 18 transfer pairs positive). Removing non-leaf image content via segmentation shows directional benefit (mean +0.066, p = 0.062, n = 36 paired observations) that is consistent across two independent segmentation methods but does not reach conventional significance. A self-supervised ViT control (DINOv2 linear probe) exhibits equivalent cross-dataset collapse to CNNs, ruling out architecture inductive bias as the primary driver and pointing to acquisition-condition shift. Adaptive batch normalization uniformly harms transfer performance, with harm magnitude correlating with source-target label-prior divergence and model depth (Spearman rho = 0.621, p = 0.009). Grad-CAM attribution analysis on 12 sampled predictions does not distinguish correct from incorrect cross-domain predictions (p = 0.462), indicating that common attribution proxies are insufficient for diagnosing shift at practical sample sizes. We document all frozen results, prespecified analysis criteria, and reproducibility artifacts in a public repository with SHA-256 integrity verification. This work establishes a rigorous empirical baseline for understanding cross-dataset generalization in agricultural computer vision and identifies both effective (augmentation) and ineffective (AdaBN) adaptation strategies.

---


### 37. [Statistical Testing for Multiple Instance Learning via Selective Inference with Applications to Computational Pathology](https://arxiv.org/abs/2609.31712)

**<font color=#1a73e8>作者：</font>** Noriaki Hashimoto, Shuichi Nishino, Teruyuki Katsuoka 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiple instance learning (MIL) is widely used in computational pathology because it enables weakly supervised analysis of whole-slide images (WSIs) without requiring patch-level annotations. In attention-based MIL, instances with high attention scores are often interpreted as diagnostically important regions and used as visual explanations. However, attention scores alone cannot determine whether selected high-attention instances are significantly different from normal instances, limiting the reliability of attention-based explanations. In this paper, we formulate the evaluation of high-attention instances as a statistical hypothesis testing problem. Specifically, we assess whether a selected high-attention instance significantly deviates from a representative normal reference instance selected based on feature similarity. A major challenge is that both the target instance and the reference instance are selected through data-dependent procedures, rendering standard hypothesis testing invalid. To address this issue, we introduce a selective inference (SI) framework that explicitly accounts for the selection events induced by attention-based instance selection and adaptive reference selection, thereby enabling the computation of valid selective $p$-values conditional on these events. Experiments demonstrate Type-I error control on synthetic and MNIST-based data and practical applicability to pathological WSIs, with higher statistical power than the conventional over-conditioning approach.

---


### 38. [Fysiverse-3D-SimReady Technical Report: Agentic Physical Simulation for Pragmatic 3D World Reconstruction](https://arxiv.org/abs/2609.31715)

**<font color=#1a73e8>作者：</font>** Lintao Wang, Mingyang Sun, Yang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic recognition requires visual perception to move beyond static scene understanding and produce structured scene representations that support the perception--reasoning--action loop. Existing single-image 3D generation methods, however, mainly produce visually plausible object assets rather than simulation-ready scene states. When independently generated meshes are composed in a shared space, they may fail to align with the input camera, violate gravity, interpenetrate nearby objects, or become unstable under physics simulation. We present Fysiverse-3D-SimReady, a grounded refinement framework for reconstructing simulation-ready multi-object scenes from a single RGB image with instance and ground prompts. The method places generated object meshes into a shared gravity-aligned scene, refines their camera-space poses through differentiable rendering, and corrects scene-level supports and contacts for stable physical execution. The scene is then used by an agentic simulation workflow, which converts a scene-specific task goal into an executable physics rollout rendered from the original camera view. Experiments show that Fysiverse-3D-SimReady improves input-view alignment, contact plausibility, and physical stability over existing single-image reconstruction and scene generation baselines, while enabling goal-conditioned physical interactions from a single image.

---


### 39. [PanOVOcc: Panoramic Embodied Open-Vocabulary Occupancy Mapping with Long-term Spatial Voxel Memory](https://arxiv.org/abs/2609.31716)

**<font color=#1a73e8>作者：</font>** Di Kuang, Mengfei Duan, Yuhang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Persistent semantic occupancy mapping is essential for embodied scene understanding. However, perspective-based systems provide limited spatial coverage, while existing panoramic methods primarily predict local volumes from single observations. We introduce PanOVOcc, a training-free framework for persistent open-vocabulary semantic occupancy mapping from panoramic sequences. PanOVOcc unifies panoramic SLAM, open-vocabulary perception, and long-term spatial voxel memory within an online architecture, continuously integrating geometric and semantic evidence into a global, language-queryable map. To facilitate systematic evaluation of this setting, we establish Pan-Replica and Pan-Holo360D, two benchmarks pairing continuous panoramic RGB-D sequences with scene-level semantic occupancy ground truth across synthetic and real-world scenes. Compared with the strongest evaluated baseline for each metric, PanOVOcc improves occupancy IoU and semantic mIoU by absolute +20.03 and +7.06 on Pan-Replica, and by +43.26 and +20.16 on Pan-Holo360D, respectively. The source code and the established benchmarks will be available at this https URL.

---


### 40. [LatentReRig: An SDF-Based VAE with Dual Decoders for Latent-Space Deformation Conditioning](https://arxiv.org/abs/2609.31720)

**<font color=#1a73e8>作者：</font>** Daniele Dolci, Fabrizio Poggioni, Carlo Melchiorri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transferring deformation between characters with different geometry and topology is challenging because conventional rigs encode behaviour through character-specific structures and correspondences. We present LatentReRig, an experimental framework that investigates whether pose-associated changes can instead be represented as reusable directions in a learned geometric latent space. An SDF-based variational autoencoder is coupled with two decoders: one reconstructs the implicit field, while the other predicts target vertex positions from source geometry and latent deformation conditioning. The source geometry may be neutral or already deformed. Experiments on a controlled humanoid dataset show that several poses induce coherent latent directions across identities, particularly for broad articulated motions. These signals can guide deformation of unseen characters, but explicit predictions remain less accurate for localized changes and corrective contributions. Diagnostic comparisons with repeated SDF sampling show that inter-identity distances exceed same-geometry resampling variability on average, while pose signals exhibit different margins above this baseline. The results support the presence of reusable pose-related structure and identify stable local conditioning and accurate mesh decoding as complementary requirements for improving transfer.

---


### 41. [Where Does the Watermark Hide? Push-Pull Disentanglement for Invisible Watermark Removal](https://arxiv.org/abs/2609.31722)

**<font color=#1a73e8>作者：</font>** Jidong Yang, Huaike Yu, Qi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fixed image distortions do not cover an attacker that learns from paired clean and watermarked images. We study this paired-training threat with single-image inference: deployment uses neither the clean reference nor the watermark key, payload, or decoder. An encoder maps each image to a structural latent $g$ and an auxiliary residual latent $u$. Push supervision reconstructs the watermarked image from $D(g_w,u_w)$. Pull supervision trains the zero-auxiliary output $D(A_g(g_w;k),0)$ toward the paired clean image. At $k=1.10,u=0$, the four-method sweep gives an average BER of $0.3958$, PSNR of $31.07$ dB, and SSIM of $0.9554$. Restoring $u$ from $0$ to $0.15$ moves average BER from $0.3893$ to $0.3357$, while PSNR falls from $30.99$ to $28.23$ dB. The intervention supports decoder dependence on the auxiliary input in the evaluated setting. The accompanying theory is a conditional, post-hoc account of this behavior rather than an experimentally verified information-relocation result.

---


### 42. [Frequency-Domain AI-Generated Image Detection: Exploring Decoder and Channel Attention for Feature Refinement](https://arxiv.org/abs/2609.31723)

**<font color=#1a73e8>作者：</font>** Uday Shankar Roy, Mahbuba Jahan Minu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid progress of AI, the number of AI-generated images has increased significantly in recent years. However, the increasing variety of image generation models makes detection more difficult. In this work, we use Fast Fourier Transform (FFT) representation with EfficientNet-B0 for AI-generated image detection. EfficientNet-B0 provides a lightweight architecture that can be useful for resource-limited applications. Most frequency-domain detectors use a standard encoder to extract features from the FFT spectrum and directly pass them to a classifier. We explored a different approach by investigating ECA, U-Net, and Attention U-Net as alternatives to this direct encoder-to-classifier approach. ECA applies channel attention, while U-Net and Attention U-Net use decoder-based architectures to recover and refine spatial information in the extracted frequency features. We used a balanced subset of the MS COCOAI dataset that includes AI-generated images from five different models. Three runs were carried out for each experiment, and the average values were recorded. Experimental results indicate that EfficientNet-B0 obtained an accuracy of 84.64%, which is 4.50 percentage points higher than the ResNet-50 baseline reported in the dataset paper. EfficientNet-B0 with U-Net provided a small improvement, achieving an accuracy of 84.85%, while ECA did not increase the overall performance. EfficientNet-B0 with Attention U-Net achieved the best overall performance, with an accuracy of 85.51% and an ROC-AUC of 92.99%. This represents an improvement of 0.87 percentage points in accuracy compared to the EfficientNet-B0 baseline and 5.37 percentage points over the ResNet-50 baseline reported in the dataset paper.

---


### 43. [SWT: Self-Supervised Video Object Segmentation via Sliding, Wavelet and Transportation](https://arxiv.org/abs/2609.31725)

**<font color=#1a73e8>作者：</font>** Zhengtong Zhu, Jiaqing Fan, Hanwen Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Object Segmentation (VOS) aims to accurately segment target objects from consecutive video frames and track the changes of the objects in each frame of the video. Conventional VOS methods typically demand substantial quantities of pixel-level labeled video sequences for fully supervised learning, which limits the performance of the model in sparse video scenes, while existing VOS methods have limited adaptability to global changes in objects. Based on this observation, in this paper, we propose self-supervised VOS with Sliding window, Wavelet transform and optimal Transport (SWT), a self-supervised VOS framework entirely trained on static dataset using contrastive learning. Firstly, a rolling sample buffer reuses overlapping groups of independently sampled images across successive updates. Secondly, to address the long-distance modeling difficulty caused by simple convolutional structures, we introduce wavelet transform to expand the receptive field of convolutional kernels, thus improving the model's representational capability. Finally, we incorporate optimal transport to assist the model in finding the globally optimal match between the target across two frames, improving the model's ability to handle nonrigid deformations of objects. SWT only requires training on the COCO dataset once and achieves excellent results on five VOS datasets as well as an additional body part propagation dataset. The code will be released soon at [this https URL](this https URL).

---


### 44. [High-Capacity Robust Medical Image Exfiltration via Neural Network Weight Replacement](https://arxiv.org/abs/2609.31726)

**<font color=#1a73e8>作者：</font>** Elie Thellier, Huiyu Li, Nicholas Ayache 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative medical AI platforms allow researchers to train models on sensitive imaging data while restricting data export. However, trained models can serve as covert carriers of patient information: medical images may be encoded within model parameters and reconstructed outside the secure environment. Existing defenses rely on lightweight sanitization (e.g., fine-tuning, pruning, quantization) and limited statistical auditing, creating a realistic insider exfiltration risk. We introduce a high-capacity neural steganography attack that encodes medical images as continuous latent representations embedded into model initialization. A StyleGAN2-based adversarial autoencoder learns compact latent codes regularized to match standard weight initialization statistics, keeping embedded parameters statistically consistent with clean models. Noise injection during training improves robustness to export-time mitigation. The carrier model remains functional on its intended task and hidden images can be reconstructed directly from its weights after export. This continuous encoding enables robust and scalable exfiltration, allowing up to 99 brain MRI volumes to be embedded within a 30MB model, and remains recoverable under mitigations that disrupt prior bit-level schemes. While reconstructions are approximate rather than pixel-exact, embedded content remains anatomically recognizable and recoverable at scale, exposing a privacy risk distinct from prior bit-level approaches. Experiments on MIMIC-CXR, BraTS, and LiTS demonstrate effectiveness across modalities, tasks, and architectures, highlighting the need for structural defenses beyond parameter-level sanitization. Code is available at this https URL.

---


### 45. [GERIS: A Game-Theoretic Framework for Filtering Instance-Dependent Label Noise in License Plate Data Augmentation](https://arxiv.org/abs/2609.31731)

**<font color=#1a73e8>作者：</font>** Seyedeh Sara Jalili Shani, Rouhollah Ahmadian, Amin Rahmani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose GERIS, a game-theoretic framework for instance selection in the data augmentation phase of license plate recognition systems. During augmentation, synthetic license plate images are generated and transformed using stochastic noise to simulate real-world conditions. However, certain noise configurations lead to highly distorted, unreadable images that degrade model performance by introducing instance-dependent label noise. GERIS formulates a non-cooperative game in which each noise vector competes for inclusion in the training set based on its similarity to labeled data and its contribution to model reliability. By identifying and pruning low-quality instances, GERIS improves the overall quality of the augmented dataset. Unlike traditional black-box learning methods, GERIS offers a transparent, theoretically grounded mechanism for data filtering. Experimental results demonstrate that GERIS outperforms existing instance selection methods in terms of classification accuracy and robustness.

---


### 46. [Measuring the evolution of camera distance across a century of film](https://arxiv.org/abs/2609.31734)

**<font color=#1a73e8>作者：</font>** David Bamman, Allison Cooper, Dan Hickey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rise of computer vision and artificial intelligence has made possible new forms of large-scale computational measurement. We apply these techniques to a deep collection of 5,205 digitized films viewed in theaters between 1922-2025 (covering popular, prestigious, and independent movies) to trace the development of one of the most fundamental ways through which film communicates: by manipulating the space between the camera and its subject. This work finds abrupt changes with the rise of new technologies in sound and television, and allows us to shed an empirical light on gender disparity (women, despite having substantially less screentime than men, are disproportionately the subject of closer shots), and illustrate how animated films both inherit and break free from the norms of live-action filmmaking.

---


### 47. [LukeNet: A lightweight CNN integrated with an XAI model for Smart acute lymphoblastic leukemia detection and management](https://arxiv.org/abs/2609.31736)

**<font color=#1a73e8>作者：</font>** Md Taimur Ahad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acute Lymphoblastic Leukemia (ALL) patients require early, accurate detection to enable timely treatment and effective patient management. A Convolutional Neural Network (CNN) is well-suited for creating an end-to-end enabling environment for ALL detection and classification. However, most CNN-based ALL detection systems are theoretical and unsuitable for deployment on edge devices due to high computational demands. The Internet of Medical Things (IoMT)-enabled devices offer an opportunity to monitor ALL patients in real time. Wearables that track temperature, heart rate, oxygen saturation, and activity can deliver critical data to support timely clinical intervention and improve patient outcomes. In smart IoMT environments, a lightweight CNN is essential because connected devices often operate under limited computational power, memory, and latency constraints. To address this need, this study proposes LukeNet, a lightweight CNN integrated with explainable artificial intelligence (XAI) for an IoMT-based SMART Acute Lymphoblastic Leukemia Detection and Management System. Trained on three (3) ALL datasets and five-fold cross-validation, LukeNet achieved an impressive 99% model accuracy as well as 99% unseen test accuracy, which is higher than six state-of-the-art (SOTA) CNNs, such as DenseNet121, MobileNet, ResNet50, InceptionV3, Xception, and VGG16, as well as transfer learning models. Furthermore, LukeNet was compared with two ensemble models. In addition, explainable AI methods are integrated to highlight relevant regions in microscopic images. The novelty of this study lies in the architecture of LukeNet, which balances model depth and computational efficiency by using depthwise separable convolutions, mitigates the risk of gradient loss in deeper layers, and provides strong global and local feature extraction capabilities.

---


### 48. [Seeing the Heat: Synthesizing High-Resolution Wood Thermal Responses from Optical Imagery](https://arxiv.org/abs/2609.31737)

**<font color=#1a73e8>作者：</font>** Jingren Xie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The thermal behavior of wood is a critical factor in advanced material assembly. However, pixel-level thermal analysis remains fundamentally constrained by the low resolution and noise inherent to infrared thermography. To address this, we introduce an end-to-end computational framework that synthesizes high-resolution thermal responses directly from wood RGB images. We first establish a core physical linkage: because spatial color variation in natural wood is driven by cellular anatomy, optical intensity serves as a reliable geometric proxy for the localized solid volume fraction. By leveraging this theoretical insight, we develop an automated finite-element-method data engine that maps pixel-level optical intensity to a 3D thermodynamic voxel grid, generating high-fidelity synthetic thermal responses. We find that 1) when the thermal conductivity along the thickness direction is uniform or linear, wood RGB images and their corresponding thermal responses exhibit extreme morphological similarities, and the lateral thermal diffusion acts as a low-pass filter that smooths out high-frequency details; 2) when the thermal conductivity along the thickness direction is random, such morphological similarities are destroyed, and wood's 3D structure dominantly governs its thermal response. We further utilize these synthetic thermal responses to supervise a neural surrogate model built upon the DINOv3 foundation model. Our results demonstrate that the neural surrogate model successfully internalizes the governing thermodynamic laws, thereby bypassing computationally expensive simulations and enabling high-resolution thermal inference. This methodology effectively bridges the semantic and thermodynamic domains, unlocking systematic, pixel-level analysis of fine-grained wood thermal responses. Project: this https URL

---


### 49. [Beyond Volume Overlap: Surface Matching for Topology-Aware Coronary Artery Segmentation](https://arxiv.org/abs/2609.31740)

**<font color=#1a73e8>作者：</font>** Rafael Velasquez, Esther Puyol-Antón, Pablo Arbeláez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate coronary artery segmentation on coronary computed tomography angiography (CCTA) is essential for diagnosing coronary artery disease. Deep networks are conventionally trained and evaluated with the Dice coefficient, but volume-overlap metrics are poorly suited to thin, tubular anatomy: since most voxels belong to a few thickproximal segments, a missing distal branch barely affects Dice despite severely disrupting the connectivity required for clinical use. We introduce a surface metric that matches predicted and reference surface points via bipartite assignment under a localized, vessel-radius tolerance, reporting precision, recall, and F1 with decoupled false positives (spurious branches) and false negatives (missed branches) a distinction the symmetric Dice cannot make. With it we show that a strong Dice-trained baseline omits far more vessel surface than it hallucinates, an asymmetry its high Dice hides. Building on this, we propose a differentiable surface loss that simultaneously suppresses spurious mass and recovers absent structure, validated by fine-tuning three backbones (nnU-Net, SwinUNETR, NexToU) on two public benchmarks (Image-CAS, ASOCA). Against a matched-epoch control, it significantly improves surface F1 by recovering missed distal vessels at comparable Dice. Our findings argue for measuring and optimizing the vessel surface, not the volume it overlaps. Code

---


### 50. [PEEL-DDPM: Physics-Enabled Evidential Learning for the Denoising Diffusion Probabilistic Model](https://arxiv.org/abs/2609.31742)

**<font color=#1a73e8>作者：</font>** Ge Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Normal-inverse-gamma (NIG) regression is not identifiable from its marginal Student-t likelihood: three combinations of four NIG parameters are determined, leaving one degree of freedom. We introduce PEEL-DDPM, a physics-enabled evidential learning framework for denoising diffusion probabilistic models. A measurement-conditioned DDPM is first trained with epsilon-MSE and then frozen. Its complete reverse trajectory produces a reconstruction, whose residual from the known training object is modeled by a final-image evidential network. The network learns only the identifiable Student-t coordinates, while repeated scanner-noise realizations and repeated diffusion trajectories provide a nested Monte Carlo estimate of final-image aleatoric variance, separated into scanner-induced and sampler-induced components. This measured variance resolves the remaining NIG ambiguity and yields a decomposition of predictive uncertainty into measurement, diffusion, and epistemic terms.
The method uses sequential training without a cross-loss weighting coefficient. In a feasibility study on eight held-out objects, empirical central-interval coverages were 49.3%, 80.3%, 90.1%, and 95.6% for nominal 50%, 80%, 90%, and 95% intervals. The mean squared residual was 0.967 times the mean predicted variance, and a single-image aleatoric head achieved pooled Spearman correlation 0.785 against an independent nested reference. Across five dose levels, scanner-induced variance showed a log-log dose slope of -1.15, whereas sampler-induced variance remained nearly dose independent with slope -0.01. These results support PEEL-DDPM as a practical route to identifiable and physically interpretable uncertainty quantification in diffusion-based image reconstruction.

---


> [!TIP]
> 当前位于：**1-50**（第 1/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
