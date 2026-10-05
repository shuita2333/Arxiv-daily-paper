# 📦 其他研究 | 2026年10月06日

> 本类共 **260** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-260](./part-06.md)

---

### 1. [Hybrid Machine Learning-Assisted Raman Spectroscopy with Generative Feature Augmentation for Pharmaceutical Identification](https://arxiv.org/abs/2610.02224)

**<font color=#1a73e8>作者：</font>** Quach Thi Thai Binh, Ton Nu Quynh Trang, Thang B. Phan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rapid and reliable identification of pharmaceutical residues is important for safeguarding public health, ensuring food safety, and enabling practical Raman-based screening. In this study, we propose HyMLRaman, a hybrid Raman spectroscopy framework that combines deep spectral feature extraction, generative models, and classical machine-learning classifiers to identify six pharmaceutical compounds, including amoxicillin, chloramphenicol, ciprofloxacin, tetracycline, ibuprofen, and paracetamol. Raman spectra are converted into spectral images and encoded with several deep neural-network backbones, among which EfficientNet-B3 yields the most effective representation. The resulting 1536-dimensional embeddings are then used to train downstream classifiers, including SVM, KNN, logistic regression, random forest, XGBoost, and ANN, using stratified 10-fold cross-validation. The hybrid EfficientNet-B3--SVM configuration achieves the strongest baseline performance, reaching 96.31% accuracy and a macro-F1 score of 96.36%, outperforming the standalone CNN baseline. To address limited-data conditions, a generative model, a DDPM-based feature augmentation, is introduced in a PCA-reduced EfficientNet-B3 latent space. The low-data ablation results show that DDPM augmentation provides selective benefits, particularly for KNN with reduced training fractions, and that its effect remains classifier-dependent. Finally, an application-level Raman Pharmaceutical Analyzer demonstrates the feasibility of embedding the trained model into an interactive Raman analysis workflow. These results suggest that HyMLRaman provides a practical and interpretable route for rapid Raman-based pharmaceutical screening.

---


### 2. [The Price of Greenwashing: Algorithmic Verification and Market Discipline using Conformal Machine Learning](https://arxiv.org/abs/2610.02225)

**<font color=#1a73e8>作者：</font>** Sourav Bose, Taoufik Bouraoui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While corporate sustainability mandates are expanding, the systemic reliance on self-reported emissions data exposes financial markets to pervasive greenwashing. Current literature relies heavily on subjective ESG ratings or textual sentiment analysis, leaving a critical econometric gap in objectively quantifying physical climate realities. To resolve this information asymmetry, we fuse U.S. SEC financial fundamentals with facility-level EPA greenhouse gas registries to establish a mathematically guaranteed baseline of physical corporate emissions. Leveraging a gradient boosting architecture and Mondrian Conformal Prediction, we quantify the shortfall between self-reported data and this algorithmic baseline into a novel Conformal-Weighted Continuous Divergence (CWCD) metric. Evaluating this divergence via a cross-sectional lead-lag econometric design, we uncover a robust mechanism of market discipline: algorithmic emissions divergence exhibits a severe, statistically significant negative relationship with subsequent market valuation (Tobin's Q) and operational profitability (ROA). Providing definitive evidence against the market blindness hypothesis, this study proves that institutional capital actively prices environmental deception not merely as an ethical lapse, but as a leading indicator of fundamental corporate mismanagement. Ultimately, these findings provide the quantitative justification necessary for asset managers and regulators to deploy algorithmic auditing infrastructure at scale.

---


### 3. [State-Space Unlearning for Non-Stationary Bias in Land Surface Forecasting](https://arxiv.org/abs/2610.02248)

**<font color=#1a73e8>作者：</font>** Anidipta Pal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operational land surface forecasting systems built on Mamba-family Structured State Space Models absorb non-stationary confounding events (unrecorded irrigation booms, dam-operation shifts, sensor recalibrations) into their state-transition matrices, silently biasing NDVI, LST, and crop phenology predictions long after the physical cause ends. This paper introduces SSU-LSF (State-Space Unlearning for Land Surface Forecasting), the first machine-unlearning framework purpose-built for geoscientific Mamba-based SSMs. We develop EKFac influence functions specialized to the Mamba state matrices via a closed-form matrix-exponential gradient, use spectral-radius-weighted elbow thresholding to localize a temporal confounding footprint $\Phi$, and apply Hessian-free projected gradient ascent within a KL-divergence trust region augmented by spatial total-variation (TV) regularization. Proposition 1 establishes that residual confounding is bounded by $\mathcal{O}\big((1-\rho(\bar{A})^{T_c})/((1-\rho(\bar{A}))\mu)\big)$, which grows with the window length $T_c$. Across three heterogeneous benchmarks and eleven baselines, SSU-LSF achieves confounding reduction rates of $0.773$ (CropHarvest), $0.821$ (NDVI-LST), and $0.859$ (ERA5), with worst-case clean-domain RMSE degradation of $4.2\%$ on ERA5, converging in 3--5 epochs at $8.4\times$ lower GPU-cost per unlearning request than full retraining. Code: this https URL

---


### 4. [Nearest-neighbour baselines for fingerprint prediction from MS/MS spectra under different assumptions](https://arxiv.org/abs/2610.02249)

**<font color=#1a73e8>作者：</font>** Ling Min Serena Khoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It has recently been shown that nearest-neighbour retrieval provides a strong baseline for molecular fingerprint prediction from MS/MS spectra, with several variants matching or outperforming current deep learning models (Khoo and Barzilay, 2026; Liu et al., 2026; Gupta et al., 2026). Importantly, "nearest neighbour" encompasses a family of retrieval methods that differ in the information assumed to be available at inference. In this report, we systematically compare several nearest-neighbour variants and show how these differing assumptions affect performance. Our goal is to establish stricter baselines that enable more rigorous benchmarking and better measure progress in this area.

---


### 5. [Rank-Aware Speculative Sampling for Diffusion Draft Trees](https://arxiv.org/abs/2610.02251)

**<font color=#1a73e8>作者：</font>** Marcello Bullo, Yanxiao Liu, Öykü Sıla Güner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative sampling accelerates diffusion generation by verifying inexpensive draft states in parallel while preserving the target law. Recent tree-based methods allocate the parallel compute budget more effectively than single-chain drafts, as demonstrated by Diffusion Greedy Rejection Sampling (D-GRS). D-GRS generates $K$ conditionally independent candidates per node, and sequentially tests them in their generation order. Yet the sampled candidates admit an informative ranking without additional target-model evaluations. To exploit this, we introduce Rank-Aware Speculative Sampling (RASS), a verification rule for speculative draft trees based on rank-aware list coupling. RASS orders draft candidates along the proposal-target mean displacement and samples a rank with weights optimized to minimize total variation between the selected-proposal and target laws. Finally, the selected candidate is maximally coupled with the target, with residual correction ensuring exact sampling for any choice of rank weights. We evaluate RASS on a Gaussian-mixture target, unconditional pixel-space generation on FFHQ, conditional generation on CIFAR-10, and latent diffusion with Stable Diffusion 3.5 using COCO2014 prompts. Measured by the ratio of standard to speculative sampling's target-model evaluation counts, RASS improves on D-GRS across the evaluated settings, with gains reaching approximately 20% on CIFAR-10 at matched compute budgets.

---


### 6. [Counterfactual Predictions in Scientific Emulators Without Controlled Experiments](https://arxiv.org/abs/2610.02252)

**<font color=#1a73e8>作者：</font>** Dingling Yao, Kahaan Gandhi, Valentin Duruisseaux 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many scientific questions require reasoning about what was never observed: What if the conditions, interventions, or history had been different? Models can predict accurately on observed data yet fail on such what-if queries when correlated inputs are varied independently. A common remedy is to add controlled simulation data in which these factors are explicitly disentangled, but this requires access to a simulator, can be computationally expensive, and inherits the simulator's modeling assumptions. We introduce ReRoute, a framework for targeted scientific what-if prediction that combines factual data with partial mechanistic knowledge, without requiring controlled intervention data for adaptation. ReRoute fixes the queried input of a pretrained backbone to a reference value, reintroduces its variation through a known mechanistic pathway, and fine-tunes on the original factual data, while leaving downstream effects to the learned dynamics. We provide a causal identification result for this construction under explicit structural assumptions, with the core argument machine-checked in Lean. After showing that ReRoute achieves highly accurate counterfactual predictions in a controlled advection-diffusion system where exact responses are available, we turn to state-of-the-art climate emulation. On held-out coupled-climate interventions, ReRoute reduces aggregate climate error by 18.2-31.8% under severe CO$_2$ distribution shifts while preserving skill under standard conditions, at a small fraction of the cost of retraining on additional controlled simulations, without even accounting for the substantial expense of generating such data. Finally, on an emulator trained from historical ERA5 reanalysis, where no counterfactual reference exists, ReRoute preserves substantially more of the surface warming implied by the observed boundary conditions under a fixed-CO$_2$ counterfactual.

---


### 7. [Approximation Property of Dropout Neural Networks: Sobolev Rates and Confidence Bounds](https://arxiv.org/abs/2610.02253)

**<font color=#1a73e8>作者：</font>** Jia-He Yao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The universal approximation property of dropout neural networks does not by itself describe the network size required for an accurate random realization. In this work, we study approximation of the unit ball of $W^{n,\infty}([0,1]^d)$ by ReLU networks whose edges are retained independently with probability $p$. The approximation error is measured uniformly over the input domain, and the guarantee holds with probability at least $1-\delta$ for a single sampled network. We construct networks of constant depth and size $\widetilde O_{n,d}(p^{-9}\varepsilon^{-\max\{d/n,2\}} \log(1/\delta))$. The construction combines bounded local subnetworks, localization on a successful approximation event, and a multiscale Taylor decomposition. Conversely, Sobolev capacity imposes a lower bound on the number of surviving edges, while approximation of a fixed affine function requires an output-layer cost of order $((1-p)/p)\varepsilon^{-2}\log(1/\delta)$ at sufficiently high confidence. For fixed $p\in(0,1)$ and $\delta<\min\{1/2,1-p\}$, the upper and lower bounds match in the accuracy exponent under a fixed or logarithmic depth budget. When $d\leq2n$, they also match in confidence up to logarithms of accuracy. We extend the lower bounds to $W^{n,r}$ targets with $L^s$ error, and distinguish this extension from the upper bound for $W^{n,\infty}$. The optimal retention dependence and logarithmic factors remain open.

---


### 8. [MACTS-EM: Multi-Agent Collaborative Time Series Forecasting with Emergent Memory](https://arxiv.org/abs/2610.02255)

**<font color=#1a73e8>作者：</font>** Ahmad Shahi, Mamehgol Yousefi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting remains a critical challenge across numerous domains. Despite significant advancements, existing approaches struggle with complex phenomena such as regime shifts, cross-domain knowledge transfer, and multimodal data integration. This paper introduces Multi-Agent Collaborative Time Series Forecasting with Emergent Memory (MACTS-EM), a novel framework where specialised agents collaborate to achieve superior forecasting performance. The MACTS-EM architecture integrates: (1) domain-specialised forecasting agents for pattern recognition, anomaly detection, causal inference, and uncertainty quantification; (2) a meta-cognitive layer for dynamic agent allocation; (3) an emergent memory mechanism enabling cross-domain pattern transfer; (4) multimodal contextual integration; and (5) adversarial robustness components. Evaluation across financial markets, climate patterns, energy consumption, and pandemic propagation demonstrates that MACTS-EM outperforms existing approaches in most scenarios, with 8-12% improvement in forecasting accuracy, 22-27% better zero-shot transfer capability, 16-21% enhanced resilience during regime shifts, and 15-18% faster recovery after distribution shifts. Our findings suggest that collaborative, agentic approaches to time series forecasting represent a promising direction beyond traditional architectures, particularly for complex real-world scenarios requiring multi-resolution temporal understanding and contextual adaptation.

---


### 9. [TRACE: A Reproducible Benchmark for Electricity Price Forecasting with Official Operational Text](https://arxiv.org/abs/2610.02256)

**<font color=#1a73e8>作者：</font>** Xinyi Yi, Moy Yuan, Ioannis Lestas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electricity price forecasting (EPF) supports scheduling, bidding, and risk management in electricity markets, yet existing benchmarks focus mainly on numerical inputs, leaving the forecasting value of forecast-time textual context insufficiently evaluated. We introduce TRACE, a reproducible benchmark of 7,300 zone--day instances pairing prices from five zones in a major U.S. market with official operational text available at the forecast cutoff. TRACE reconstructs official operational text at each cutoff, preventing post-cutoff information leakage. We evaluate TRACE for semantic alignment and forecasting value. Semantic assessments align with central movement and both tail risks in ground-truth prices, most consistently for upper-tail price risk. Forecasting value is reflected in a median 7.4\% reduction in upper-tail pinball loss across time-series foundation models. A controlled cross-day text-mismatch ablation reverses the gains, falling below the no-text baseline.

---


### 10. [Parameter-Free Interval-Dynamic Regret under Heavy-Tailed Noise](https://arxiv.org/abs/2610.02258)

**<font color=#1a73e8>作者：</font>** Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online convex optimization with one unbiased stochastic subgradient per round and an unknown finite conditional $p$th noise moment, $1<p\le2$. For every fixed interval $I$ of length $n$ and comparator path with $\Lambda_I=1+P_I/D$, one learner achieves
\[ E[Regret_I(u)]\le\min(GDn, C[GD\sqrt{n(\Lambda_I+\log^2(2T))} +\sigma Dn^{1/p}(\Lambda_I+\log^2(2T))^{(p-1)/p}]). \]
The learner uses none of $G,\sigma,p,I,P_I$, and the constant is universal. Interval adaptation adds to comparator complexity, preserving the distinct mean-gradient and noise exponents. The analysis controls calibration in expectation and limits the cost of observation-scale changes. Its general theorem compares to distributions over predictably available experts with relative-entropy dependence on a nonuniform prior. A common prior favors long windows and long restart lengths. With the statistics supplied, the interval cost becomes $1+\log(T/n)$, including the optimal full-horizon static rate. A change-of-measure lower bound identifies the noise power of this logarithm for learners retaining a full-horizon optimal guarantee, under explicit conditions. Static comparisons and deterministic partitions follow from the same decisions.

---


### 11. [MintFlow: Minimal Trajectory Intervention for Constrained Flow Matching](https://arxiv.org/abs/2610.02260)

**<font color=#1a73e8>作者：</font>** Yesom Park, Kelvin Kan, Qifan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flow matching models excel at generative modeling, and many downstream applications require their samples to satisfy prescribed constraints, such as observed measurements and physical laws. However, existing constrained samplers often face a trade-off: \textit{enforcing constraints can substantially displace samples from the pretrained data distribution}. To address this trade-off, we introduce \textbf{MintFlow}, a training-free constrained sampling framework that formulates constraint enforcement as a minimal intervention on the pretrained flow trajectory. MintFlow seeks the minimal perturbation of an intermediate flow state such that its subsequent evolution under the pretrained flow field satisfies the target constraint. By minimally perturbing the flow state while keeping the pretrained flow field unchanged, MintFlow enforces the constraint while minimizing unnecessary deviation from the pretrained distribution. An adjoint formulation yields a closed-form expression for this perturbation, eliminating expensive iterative optimization. Furthermore, MintFlow adaptively selects the intervention time to balance the required perturbation magnitude with its amplification by the remaining flow. Across a range of tasks in generative vision and physical system modeling, MintFlow achieves competitive constraint satisfaction while preserving the pretrained generative distribution substantially better than state-of-the-art constrained methods.

---


### 12. [From Mathematical to Executable Certificates for Machine Unlearning](https://arxiv.org/abs/2610.02268)

**<font color=#1a73e8>作者：</font>** Ziyu Zhao, Xinyu Wang, Xiaowen Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning is needed when data must be removed because of deletion requests, outdated records, or data-quality concerns, while retraining from scratch can be costly. Certified machine unlearning methods provide mathematical guarantees, while deployed systems release concrete finite-precision artifacts produced by software. To bridge the gap between mathematical guarantees and practical deployment, we introduce Executable Release Certification (ExecCert), a release-time layer that certifies the candidate artifact considered for release. ExecCert either closes a method's native certificate for the executed candidate or applies Retraining-Reference Release Verification (RRV) to certify fidelity to current retain-set retraining. Sequential deletion makes the latter nontrivial because the exact retain-set reference and the stored numerical state evolve separately. For frozen representations with a mutable ridge head, we develop an incremental realization of RRV that maintains certified evidence across deletion requests rather than reconstructing it at each release. On four published unlearning implementations, ExecCert preserves valid certificates, changes release decisions, tightens conservative bounds, and identifies the retraining-reference fidelity supported by concrete outputs. In sequential-service experiments, RRV eliminates false releases caused by stored-equation verification while closely tracking realized error, and incremental certification remains cheaper than both fresh and maintained verified-factor alternatives once release checks become sufficiently frequent.

---


### 13. [CLEAN: Psychometrically Consistent Incremental Cognitive Diagnosis under Concept-Space Expansion via Architectural Isolation](https://arxiv.org/abs/2610.02278)

**<font color=#1a73e8>作者：</font>** Tao He, Jinxing Xiang, Fan Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cognitive diagnosis (CD) is a fundamental task in intelligent education that profiles learner proficiency over knowledge concepts. In real-world learning platforms, newly added items continually introduce previously unseen concepts, necessitating dynamic expansion of the underlying concept space. Yet existing incremental CD models assume a fixed concept space, allowing gradients from new items to overwrite historical pathways and induce catastrophic forgetting. More critically, these methods rely solely on soft constraints to preserve historical diagnoses. Such constraints may fail to satisfy the requirement of diagnostic invariance after incremental updates, a requirement known as psychometric consistency in cognitive diagnosis. Therefore, we propose CLEAN (Continual Learning with Expandable and Architecturally Isolated Networks), a novel incremental CD framework supporting concept-space expansion while providing structural guarantees for pointwise invariance of historical diagnoses. Specifically, CLEAN first introduces a strict topological bipartition protocol, freezes historical diagnostic functions and applies deterministic orthogonal column masking to sever gradient interference. Second, to accommodate concept expansion, expandable full-rank branches with micro-variance initialization are deployed to learn novel concepts. Finally, to verify that this architectural design achieves invariance by construction, we formalize Representation Drift (RD) to quantify the perturbation of historical traits. Extensive experiments on three large-scale educational datasets demonstrate that CLEAN achieves zero RD, preserving old-item metrics identically to static anchors through architectural isolation while remaining competitive with or superior to strong continual-learning baselines on new items.

---


### 14. [MuLoRA: Spectrally Balanced Low-Rank Adaptation for Continual Learning](https://arxiv.org/abs/2610.02283)

**<font color=#1a73e8>作者：</font>** Junkang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) provides a parameter-efficient approach to continual learning, but its nominal rank can conceal a loss of effective adaptation capacity. We identify \emph{spectral plasticity collapse}: during sequential adaptation, update energy becomes concentrated in a small subset of singular modes, leaving much of the available low-rank space underutilized. This exposes a limitation of interference avoidance alone: protecting historical representations does not ensure that the remaining adaptation capacity is responsive to new tasks or effectively utilized. To address this problem, we propose \texttt{MuLoRA}, which jointly controls capacity allocation and utilization. First, historical whitening identifies input directions with strong current-task response relative to accumulated historical response, yielding a task-adaptive basis that remains fixed during training. Second, approximate polar orthogonalization of momentum updates reduces spectral concentration within theselected space. An orthonormal basis connects these mechanisms by transferring the factor-update spectrum exactly tothe induced weight update. We establish a max--min characterization of exact subspace selection and derive cumulative spectral bounds under controlled cross-step anisotropy. Across five class-incremental benchmarks and eight incremental settings, \texttt{MuLoRA} achieves the highest mean accuracy in 15 of 16 reported metrics.

---


### 15. [Effects of interpulse-interval variation on deep-learning classification of bat vocalizations](https://arxiv.org/abs/2610.02284)

**<font color=#1a73e8>作者：</font>** Welmoed R. Eversteijn, Burooj Ghani, A. Leonie Baier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal context may aid automated bat-species classification, but the contribution of specific features remains unclear. We investigated whether variation in the interpulse interval (IPI)-the time between consecutive call onsets-provides species-discriminative information and whether transformer-based models are more sensitive to this information than convolutional neural networks. We created two matched datasets from European bat recordings: a natural-IPI condition retaining the original call timing and a normalized-IPI condition in which call onsets were spaced at 50-ms intervals. EfficientNet-B0 and PaSST were fine-tuned and evaluated within each condition. In an additional experiment, each architecture was trained separately on natural-IPI and normalized-IPI recordings, and evaluated on the same natural-IPI test set. Finally, the pretrained classifiers BatDetect2 and BAT were evaluated on both conditions. Within-condition IPI normalization had model-dependent effects. PaSST accuracy differed little between the natural-IPI ($71 \pm 2.3\%$) and normalized-IPI ($70 \pm 6.3\%$) conditions, whereas EfficientNet accuracy increased from $47 \pm 4.7\%$ to $57 \pm 3.9\%$. PaSST exceeded EfficientNet under both conditions. In the cross-condition evaluation, models trained on natural-IPI recordings outperformed those trained on normalized-IPI recordings on the natural-IPI test set: accuracy decreased from 54% to 50% for EfficientNet and from 65% to 57% for PaSST. BatDetect2 and BAT differed little between IPI conditions. Overall, we found limited support for the hypotheses that natural IPI variation contributes substantially to bat-species classification and that it is used more effectively by transformer-based than CNN-based models. Nevertheless, the cross-condition performance decrease shows that results obtained under normalized conditions may not transfer fully to natural recordings.

---


### 16. [Diffusion-Based Synthetic Data Pretraining for Enhancing Activity Recognition](https://arxiv.org/abs/2610.02292)

**<font color=#1a73e8>作者：</font>** E. Riveros, D. Vega-Oliveros, A. Soriano-Vargas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human activity recognition (HAR) is increasingly important for healthcare, well-being, and daily monitoring ap- plications, for which detecting alimentary activities such as eating and drinking can provide actionable insight into dietary habits and chronic disease management. HAR systems, however, often underperform on subtle and underrepresented classes, limiting their utility in real-world dietary monitoring. This work builds upon CABiGRU, a convolutional architecture with Bidirectional GRU layers, multi-head attention, and residual connections, designed to capture discriminative temporal patterns from smart- watch accelerometer, gyroscope, and magnetometer data. To improve CaBiGRU's generalization and reduce underfitting in the minority class, we leverage synthetic sensor data windows using a diffusion model and adopt a two-stage training strategy: pre-training CABiGRU on synthetic data, followed by fine-tuning on the real-world data. On the DEO (drinking/eating/other) dataset, the proposed pipeline achieves a balanced accuracy of 90.6%, improving over a strong supervised baseline and showing the benefits of diffusion-based synthetic pre-training for recognizing alimentary activities and representing a step forward dealing with unbalanced classes. These results suggest that combining diffusion-generated data with targeted fine-tuning enhances robust recognition of dietary behaviors, supporting more reliable deployment in healthcare and nutrition-monitoring settings.

---


### 17. [$Ψ$-Resilience: Model-Free Feature Importance from 1D Topological Signals](https://arxiv.org/abs/2610.02299)

**<font color=#1a73e8>作者：</font>** Fabian Galis, Darian Onchis, Pedro Real Jurado  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce $\Psi$-Resilience, a model-free feature importance method that derives explanations directly from the data itself via 1D topological signals. Our method constructs a class-disagreement landscape by estimating class-conditional densities and taking their pointwise absolute difference along the feature axis. Then, the 0-dimensional persistence of this 1D signal defines a resilience functional that aggregates only those topological features that survive perturbations up to a robustness scale which is set by the user. This gives us a context-robust importance score that is inherently auditable via the underlying 1D landscapes and their persistence. We evaluate our method on both synthetic and real datasets. On synthetic generators with specified ground-truth importance, $\Psi$-Resilience recovers the ranking of features with high fidelity, achieving Spearman rank correlations up to 0.8 and performing competitively with multiple feature importance methods, including SHAP and mutual information. On real datasets with no known ground truth, our technique agrees with these methods, with correlations up to 0.9. These results show that $\Psi$-Resilience is a stable explanation method that enables rigorous, distribution-level auditing of feature importance without relying on a predictive model.

---


### 18. [Keep It CALM: Analyzing the Limits of Global Unsafety in Text-to-Image Generation](https://arxiv.org/abs/2610.02300)

**<font color=#1a73e8>作者：</font>** NaHyeon Park, Minhyun Lee, Hyunjung Shim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training-free safeguards for text-to-image generation often rely on a reusable safety signal, such as an unsafe direction or global toxic subspace, applied broadly across prompts. We provide a controlled geometric analysis of this global-unsafety assumption and reveal a consistent coverage-selectivity trade-off: compact unsafe subspaces fail to cover heterogeneous unsafe semantics, whereas broader aggregation increasingly distorts safety-adjacent benign prompts. Motivated by this finding, we propose CALM (Counterfactual Adaptive Local Modulation), a training-free safeguard that replaces uniform global removal with prompt-local counterfactual correction. Using matched unsafe-benign anchors, CALM routes each prompt to active unsafe categories, minimally edits only violating token representations toward the safe side, and suppresses positively aligned unsafe residual components. Across broad evaluation, CALM significantly improves unsafe content suppression while preserving benign utility, demonstrating that local counterfactual correction provides a more selective alternative to global unsafe signal removal.

---


### 19. [SCION: Scene Composition with Instanced Neural Primitives](https://arxiv.org/abs/2610.02322)

**<font color=#1a73e8>作者：</font>** William Koch, Amogh Joshi, Cyrus Vachha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world scenes are compositional: bricks, blades of grass, pebbles, and tree leaves recur across human-built and natural environments. Existing neural scene representations model these elements independently. Most 3D Gaussian Splatting and follow-up abstraction and compression methods treat each element as unique, fitting millions of independent Gaussians per scene. Prior methods like Splat and Replace fit template objects, but they require mostly manual selection of repeated elements. As a result, these representations store redundant parameters and provide weak manipulation handles for downstream tasks. We introduce SCION, a hier- archical compositional scene representation that replaces independent Gaussians with a compact vocabulary of reusable primitives and lightweight world-space instances that place transformed copies throughout the scene. We fit this represen- tation to multi-view captures via a joint optimization over discrete and continuous scene parameters, combining two-level densification over splats and instances with an adversarial loss that preserves detail across shared primitives. The recovered structure yields a compact, controllable representation while maintaining high quality even at 1.2 MB. SCION achieves rate-distortion favorable to existing Gaussian compression methods, and it enables instance-level scene editing and animation without retraining. Our results show that neural scene representations need not memorize scenes as independent primitives; they can discover reusable parts. Project webpage: this https URL

---


### 20. [A Multi Method Importance and Performance Efficiency Analysis of Topological Metrics for Natural Visibility Graph Based Cyber Attack Detection](https://arxiv.org/abs/2610.02342)

**<font color=#1a73e8>作者：</font>** Ali Melih Kanca, Ilker Turker  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural Visibility Graph (NVG) based analysis characterizes network traffic through topological descriptors reflecting different structural properties. However, not all descriptors contribute equally to cyber-attack classification, and extracting a large metric set can increase computational cost. This study evaluates 21 NVG derived topological metrics and investigates whether a compact subset can preserve classification capability while improving computational efficiency. Four importance analysis methods SHAP, grouped Permutation Importance, Boruta, and Recursive Feature Elimination (RFE) are integrated through a Consensus Ranking strategy. Based on this ranking, Full21, Top15, Top10, Top7, Top5, and Top3 configurations are evaluated using the CICIDS2018 dataset, a CNN classifier, and stratified 5 fold cross validation. The three highest ranked metrics are avg_clustering_coeff_median, avg_clustering_coeff_std, and avg_clustering_coeff_mean. Top3 achieved the highest observed mean performance, with 97.148% accuracy, 97.055% weighted F1 score, and an MCC of 0.9675, compared with 95.999%, 95.521%, and 0.9549 for Full21, respectively. It also reduced total runtime from 14,961.39 s to 589.22 s (96.06%). These results indicate that importance guided metric reduction can provide a compact NVG representation with higher observed mean predictive performance and substantially lower computational cost under the evaluated setting.

---


### 21. [Drive vs. Decay: On the Training Dynamics of Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2610.02344)

**<font color=#1a73e8>作者：</font>** José Lucas De Melo Costa, Seong Woo Ahn, Fabrice Popineau 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) are prone to representation collapse, typically mitigated through empirical heuristics. We develop an early-training stability theory that unifies these heuristics. Linearising the coupled JEPA gradient flow around the trivial fixed point reveals two competing effects: a driving force ($\gamma$) and a decay effect ($\sigma$). Under approximate spectral decoupling, a per-mode stability ratio $\mu_i = \gamma_i / \sigma_i$ factorises into independent data-side and predictor-side terms and the count of unstable modes tracks the rank of representations that can emerge. The framework predicts a phase boundary, which we confirm empirically across more than 800 Tabular-JEPA configurations. It also unifies predictor scaling, masking ratio, and EMA as distinct mechanisms for shifting $\mu$. Guided by this analysis, we introduce ResidualPred, a transformer predictor whose attention is biased toward the identity at initialisation; it improves both effective rank and downstream accuracy on tabular benchmarks and in I-JEPA pretraining on CIFAR-10, CIFAR-100, STL-10, and ImageNet. Our framework connects empirical collapse-avoidance heuristics to an explicit dynamical picture, yielding theory-driven stabilizers. Code is available at this https URL.

---


### 22. [Mitigating Convergence Collapse in Fixed-Target Anomaly Detectors via Kernel-Anchored Locality Regularization](https://arxiv.org/abs/2610.02345)

**<font color=#1a73e8>作者：</font>** José Lucas De Melo Costa, Fabrice Popineau, Arpad Rimmel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A family of tabular anomaly detectors trains a neural map toward a fixed target under squared-error loss and scores anomalies by the test-time residual; contraction matching, one-step rectified flow, and reconstruction autoencoders all fit this template. We characterize a convergence collapse: better optimization makes the detector worse. At convergence, the learned map tracks the target even off-distribution, so the residual signal vanishes on anomalies as well as on normal data. These detectors therefore rely on implicit non-convergence (early stopping, capacity caps) to retain signal. We argue this is structural: effective anomaly detection requires a locality constraint that blocks unconstrained extrapolation. Classical detectors (kNN, KDE, isolation forests, LOF) enforce locality explicitly; fixed-target neural detectors do not. We formalize the connection by showing that the kernel-regression analog of a fixed-target detector is a finite-bandwidth Nadaraya-Watson smoother, which we call Kernel Contraction Matching (KCM). KCM is closed-form, training-free, and CPU-efficient, yet matches established neural baselines on ADBench. Building on this bridge, we introduce the Kernel-Anchored Regularizer (KAR), which penalizes deviation of the neural prediction from a kernel-weighted average of training targets. Across collapse-prone ADBench datasets and three backbones, KAR mitigates collapse and improves AUROC under prolonged training.

---


### 23. [ArrivalBench: Agent-Generated Data Pipelines Are Correct Once and Wrong Under Time](https://arxiv.org/abs/2610.02363)

**<font color=#1a73e8>作者：</font>** Pranay Kothari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarks for agent-generated data work grade a pipeline by running it once against a fixed snapshot. ArrivalBench instead re-executes the pipeline an agent leaves behind under adversarial but replayable delivery schedules (late, duplicated, out-of-order and retried records) and requires its final state to equal a batch recomputation of the complete log. Because the oracle recomputes rather than classifies, a wrong table and a crash are distinct verdicts: a crash is visible to monitoring a team already runs, and a wrong table is not. On 40 tasks we built, our reimplementation of single-execution grading certifies 86-100% of the pipelines eleven models produce; re-executing the same artifacts finds 7.0-79.2% of the certified ones silently wrong. The gap is not produced by the repair loop: within the same model and task, pipelines repaired against the snapshot test fail replay about as often as those that passed it first time. In every model, idempotency hazards fail more often than ordering hazards. Separating a wrong answer from a crash also changes how interventions read: a hazard warning cuts one model's silent failure from 48.2% to 10.5% while raising its crash rate from 9.0% to 37.0%, so all-in failure moves only from 51.0% to 44.0%. All eleven arms were independently re-run, and rates moved by at most 5.9 points.

---


### 24. [Confidence-Controlled XAI Auditing for Pedestrian Detection under Domain Shift](https://arxiv.org/abs/2610.02364)

**<font color=#1a73e8>作者：</font>** Ruben Dario Florez-Zela  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explainability is increasingly required for perception models in intelligent vehicles, yet whether explanations remain faithful under driving domain shift is still poorly understood. This work audits post-hoc explanations of a fixed YOLOv8s pedestrian detector across PIE and JAAD using ROI-based D-Deletion, frozen confidence terciles, rank-based tests, bootstrap intervals, and Holm correction. The audit shows that deletion-based faithfulness is strongly coupled to detection strength at explanation time, with Spearman correlations between 0.70 and 0.82 for D-RISE, making naive confidence-stratified comparisons unreliable. After controlling for detection strength within fixed f0 bins, D-RISE faithfulness remains domain-dependent in the central f0 range, with PIE showing higher D-Deletion than JAAD and Holm-adjusted significance. A non-perturbative EigenCAM baseline is less faithful than D-RISE but also exhibits score coupling, suggesting that the effect is not specific to D-RISE and is related to the deletion-based evaluation setup. These results motivate confidence-controlled XAI audits for safety-critical perception under domain shift.

---


### 25. [Co-design Gym: A Unified Benchmark for Embodiment-Policy Co-optimization](https://arxiv.org/abs/2610.02366)

**<font color=#1a73e8>作者：</font>** Aviraj Newatia, Yordan Tsvetkov, Leonard Pleiss 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finding an optimal behaviour policy within a given environment is a widely studied problem in domains as diverse as games, robotics, energy infrastructure, communication networks, and multi-agent systems. Numerous benchmarks have been developed to support such research, but the vast majority assume that the agent's embodiment (design) is fixed, focusing instead on policy learning alone. Lifting this assumption gives rise to a broader class of problems in which optimizing embodiment and policy separately is highly suboptimal. An agent's embodiment strongly shapes which control policies can be discovered, while the optimal embodiment is in turn defined by the policies it admits. To help the research community study this class of problems explicitly and systematically, we introduce Co-Design Gym - a suite of benchmark environments for jointly optimizing embodiment and policy. Our environments span domains such as robotic manipulation and locomotion, multi-robot cooperation, deformable and soft dynamics, video games, electricity grids, wireless networks, F1 racing, multi-agent warehouses, and optimal control, offering 20 environment families (domains), with over 85 distinct co-design presets in total. We further contribute a systematic evaluation of representative co-design algorithms, characterizing the current state of the art. Together, these contributions lay the groundwork for cumulative, comparable progress in co-design.

---


### 26. [Traversing the Satisfaction-Diversity Frontier in Text-to-Image Diffusion](https://arxiv.org/abs/2610.02372)

**<font color=#1a73e8>作者：</font>** Kevin Zhai, Siva Rajesh Kasa, Soumya Roy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-image generation enables users to explore several images generated from the same prompt. For these generated images to be useful, each one must reflect the user's preferences, measured by a learned reward, and differ visually from the others to maintain diversity. Existing methods are limited: they either address reward and diversity separately or combine them in one aggregate score, enabling high diversity to offset low rewards. In this paper, we address these limitations by formulating generation as satisficing: every image (candidate) must satisfy a reward floor and the batch of images must satisfy a diversity cutoff. The reward floor controls the balance between worst-candidate reward and batch diversity; we show that varying this floor defines a Pareto frontier. To traverse this frontier, we introduce SatisDive, a training-free inference-time method. SatisDive uses a batch-relative reward cutoff to distinguish lower- from higher-reward candidates, emphasizing reward improvement for candidates below the cutoff and diversity among candidates above it. On Pick-a-Pic, at matched DreamSim, SatisDive improves worst-candidate reward over FK steering by up to 0.43 with FLUX.1-dev as the base model and HPSv3 as the reward, and by up to 0.70 with SANA-1.6B as the base model and ImageReward as the reward. More broadly, across their overlapping DreamSim ranges, SatisDive's satisfaction-diversity curve Pareto-dominates FK steering's curve in each setting.

---


### 27. ["I'm trying not to get hacked:" How Adults with Intellectual and Developmental Disabilities Navigate Security and Privacy Notifications](https://arxiv.org/abs/2610.02374)

**<font color=#1a73e8>作者：</font>** Hailey L. Johnson, Julia Nonnenkamp, Bilge Mutlu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Security and privacy notifications, such as login alerts, spam email warnings, and cookie consent requests, play a critical role in shaping users' responses to digital risks. Yet most notifications overlook cognitive accessibility, limiting their effectiveness for people with intellectual and developmental disabilities (IDD). We investigate how adults with IDD perceive and respond to common security and privacy notifications across mobile and web applications. Through a formative user study with seven adults with IDD, we identify three factors shaping understanding and decision-making: (1) interpretation is influenced by task and interface context; (2) unfamiliar terms, both technical and non-technical, are grounded in everyday concepts; and (3) uncertainty about outcomes leads to hesitation, avoidance, diagnostic exploration, or support-seeking. These findings lead to three design implications: (1) address context-dependent language misunderstandings beyond jargon simplification; (2) make action-outcome connections transparent; and (3) enable interdependent decision-making. Together, these insights aim to inform the design of more cognitively accessible security and privacy notifications that better support safe and supported user action.

---


### 28. [FactorSplat: Appearance-Controllable Gaussian Proxies for Medical Volume Rendering](https://arxiv.org/abs/2610.02382)

**<font color=#1a73e8>作者：</font>** Zhongpai Gao, Benjamin Planche, Meng Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transfer functions (TFs) control color and visibility in medical volume rendering, but image-trained Gaussian proxies typically bake one transfer function into their appearance. We present FactorSplat, a per-scene N-dimensional Gaussian splatting (N-DGS) proxy that accepts region-specific intensity-to-RGBA curves at inference. A local lookup applies the authored color and opacity change, while a shared functional encoder and low-rank per-Gaussian factors learn the residual appearance response. Geometry and directional appearance remain shared across presets, with visibility control and TF-aware pruning preserving the ability to hide and reveal structures. On seven CT and MR scans, FactorSplat improves mean PSNR and changed-region error over region-aware VEG across validation, interpolation, unseen composition, and out-of-distribution (OOD) edits. Across these four splits, seven-scan mean PSNR gains over VEG range from 1.10 to 1.52 dB. One checkpoint per scan supports unseen edits without retraining. At $1600^2$, the cached fast renderer averages 524 FPS with 1.17 ms TF switches. Project page: this https URL.

---


### 29. [Connectedness, Cognitive Load, and Human-AI Oversight in Cyber Operations](https://arxiv.org/abs/2610.02384)

**<font color=#1a73e8>作者：</font>** Nathan Conklin, Peng Gao, Chris North  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-assisted cyber situational awareness triggers machine-generated reasoning traces (step-by-step justifications for anomaly classifications) that a human operator is expected to review. Because cyber signals and their traces arrive faster than any operator can process, human review is the limiting constraint on oversight. The standard approach is to identify the riskiest cyber events for review using model-side signals such as confidence or uncertainty. That framing ignores the operator's cognitive capacity which varies sharply with the operational environment. We propose an alternative where the system's environmental and connectivity telemetry serves as an available, non-invasive proxy for operator load. That same telemetry determines whether the human-AI partnership can reach the broader collective for support. In a maritime platform, environmental and connectivity attributes including depth, number of active communications paths, density of the tracked contact picture, and operational tempo all carry this signal. Need for operator oversight becomes a decision that materializes as a combination of both risk and environment-derived operator capacity. We present a reference architecture for a connectedness-aware oversight engine, demonstrating everyday use cases alongside its intended incorporation into the submarine cyber-defense toolkit. Two themes emerge: 1) the operator's environmental state is itself a connectedness measurement, and 2) connectedness drives the cognitive load and defines a collective boundary in human-AI cyber operations.

---


### 30. [FlashSinkhorn 2: Block-Sparse Entropic Optimal Transport](https://arxiv.org/abs/2610.02395)

**<font color=#1a73e8>作者：</font>** Felix X.-F. Ye, Yu Chin Fabian Lim, Naigang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Streaming GPU solvers for entropic optimal transport (EOT), such as FlashSinkhorn, avoid storing the dense kernel but still evaluate all $n\times m$ point pairs in every Sinkhorn iteration. We present \textbf{FlashSinkhorn~2} (FS2), a solver for squared-Euclidean cost on low-dimensional point clouds that solves large discrete EOT problems to a prescribed marginal residual on a single GPU by coupling two stages. A coarse stage solves on cell centroids, lifts the potentials to every point and, when a sampled marginal check rejects the lift, continues on the centroids, replacing most point-level updates. A block-sparse fine stage then removes the centroid error that coarse updates cannot. Its Morton-ordered blocks support screening and fused tensor-core execution, and a threshold set by the block masses bounds each omitted tile's contribution to every row and column. On synthetic benchmarks, FS2 reaches the target residual on all 32 problems and GeomLoss multiscale on 10. On one A100, FS2 solves discrete EOT between two $1.34\times10^8$-particle measures from a cosmological $N$-body simulation, at an entropic blur equal to the mean interparticle distance, to an all-particle marginal residual below 0.01 in under 2.5 hours. To our knowledge, it is the largest discrete EOT problem solved to this accuracy within hours. For reproducibility, we release an open-source implementation at this https URL

---


### 31. [Validated Data Onboarding for AI Demand Forecasting on U.S. Building Meter Data: Design, Controlled Evaluation, and a Corrected Negative Result](https://arxiv.org/abs/2610.02397)

**<font color=#1a73e8>作者：</font>** Yixuan Liang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electric utilities and grid operators increasingly rely on machine-learning models to forecast next-day demand, and those models learn from meter data that is routinely defective: readings go missing, sensors freeze, buildings read zero for hours, and units change by a factor of 100. This report presents a data-onboarding pipeline that detects and repairs such defects before a model is trained, using only information available at forecast time, and a controlled experiment that measures whether the pipeline protects a 24-hour-ahead forecast. On hourly electricity data for twelve U.S. buildings from the public Building Data Genome 2 dataset (210,528 rows, 2016-2017), seeded, hash-logged defects touching 0.10% of the training period raised the error of a gradient-boosting forecaster by 86%; after detection and past-only repair the error returned to the clean-data level (mean absolute scaled error 0.760 clean, 1.415 corrupted, 0.729 repaired) while 93% of training targets were retained. At a defect prevalence calibrated to published field studies (1.6% of training rows) the unprotected forecaster's error reached 4.4 times that of a seasonal-naive rule, and the repaired forecaster again matched the clean baseline. The same pattern held for ridge regression and a random forest and across horizons of 1 to 24 hours. A first version of the pipeline over-cleaned natural data and made forecasts 25% worse; that result is retained, its cause is traced in the published artifacts, and the per-building calibration that corrects it is documented as a dated amendment. Every number is reproducible from pinned public inputs with SHA-256 verification, 84 automated tests and continuous integration.

---


### 32. [VisAudit: Evaluating Multimodal Agents for Visual Diagnosis and Repair](https://arxiv.org/abs/2610.02399)

**<font color=#1a73e8>作者：</font>** Shicheng Liu, Adam Kahirov, Qi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal agents are increasingly used for data visualization tasks but remain limited in autonomous review. Unlike humans, they may fail to recognize when a visualization is incorrect, determine what to change, repair it without disrupting correct content, and verify whether the intervention succeeded. Existing benchmarks largely evaluate predefined individual capabilities such as chart generation, instruction-guided editing, or defect detection, and therefore do not capture this gap in autonomous review. We introduce VisAudit, a benchmark for evaluating visualization diagnosis, repair, and verification. Given a rendered chart and configurable auxiliary evidence, including its source data table, intended text summary, and visualization code, an agent iteratively diagnoses potential defects, modifies and executes visualization code, inspects execution and visual feedback, and determines when no further intervention is needed. VisAudit defines three tracks spanning diagnosed repair, autonomous repair, and open-world verification, and contains 1,900 flawed instances across 21 chart types and 10 flaw categories, together with 300 initially correct charts. We construct the benchmark through controlled perturbations of validated source visualizations, with systematic verification and human-aligned quality control to ensure that injected defects are well-defined and recoverable from the available evidence. Experiments with leading multimodal models reveal a substantial gap from reliable autonomous review: the strongest evaluated model fully recovers only $47.4\%$ of flawed charts in the autonomous-repair setting.

---


### 33. [Efficient Neural Field Learning via Adaptive Coverage and Focused Sampling](https://arxiv.org/abs/2610.02410)

**<font color=#1a73e8>作者：</font>** Guang Zhao, Xihaier Luo, Huan-Hsin Tseng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) provide a flexible framework for modeling high-dimensional continuous fields, but their training is often inefficient due to uniform subsampling that ignores spatial heterogeneity. Existing adaptive sampling methods partially address this issue by prioritizing high-error samples, but typically operate at the point level, often leading to redundant sampling in localized regions and insufficient coverage of the domain. We propose ACES (Adaptive Coverage-aware Efficient Sampling), a structured sampling framework that improves training efficiency by decoupling coverage and importance. ACES constructs adaptive spatial partitions to ensure domain coverage and reduce redundancy, and applies region-level importance weighting to prioritize informative regions during training. We provide a theoretical analysis showing that adaptive partitioning reduces gradient variance by increasing within-region homogeneity, and that controlled bias in region-level weighting may improve optimization efficiency relative to standard unbiased estimators. Experiments on scientific field learning tasks demonstrate that ACES achieves faster convergence and lower error than uniform and pointwise adaptive sampling baselines, with the largest gains in fields with highly localized complexity.

---


### 34. [Unifying Privacy Accounting: Information Equivalence and Information Loss](https://arxiv.org/abs/2610.02414)

**<font color=#1a73e8>作者：</font>** Buxin Su, Qiaoshi Yang, Yiding Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) admits several notions, but the choice among them may affect both privacy analysis and utility. In this paper, we consider four mainstream curve-based privacy notions within a unified information-theoretic framework. For a fixed ordered pair of output distributions, we establish information equivalence among the two directional privacy profiles of $(\varepsilon,\delta)$-DP, the pair of hypothesis-testing trade-off functions, and the extended privacy-loss distribution. The exact Rényi differential privacy (RDP) curve joins this equivalence class whenever it is finite at some order greater than one. Under this mild condition, choosing among these notions changes only their semantic interpretation and computational requirements. In contrast, taking the maximum of the directional privacy profiles or compressing the RDP curve into a single zero-concentrated differential privacy (zCDP) parameter can lose information. We quantify the information loss between the exact RDP curve and its zCDP bound for standard noise mechanisms. This gap is zero for Gaussian noise but generally positive for Gaussian-mixture, Laplace, discrete Gaussian, and Poisson-subsampled Gaussian mechanisms. Moreover, this gap grows linearly with the number of independently composed mechanisms. Our information-theoretic perspective has practical consequences. At the same certified privacy level, retaining the full RDP curve rather than using zCDP reduces the required noise variance by up to $45\%$ for Gaussian-mixture noise in workloads comparable in size to the American Community Survey. For DP-SGD on Fashion-MNIST under Poisson subsampling, an RDP-based privacy accountant improves test accuracy by up to $8.73$ percentage points compared to a zCDP-based accountant when both are calibrated to the same $(\varepsilon,\delta)$ guarantee.

---


### 35. [The AI Theorist reveals excitonic structure in $α$-RuCl$_3$](https://arxiv.org/abs/2610.02417)

**<font color=#1a73e8>作者：</font>** Hongjian Zhou, Xianfan Nie, Sean Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advances in experimental instrumentation and automation generate increasingly rich datasets, but turning experimental observations into microscopic understanding remains a bottleneck in scientific discovery. To accelerate this process, we introduce AI Theorist, a system of artificial intelligence (AI) agents for autonomous discovery of physical models through hypothesis generation, first-principles calculations and evidence-driven refinement. We apply the framework to $\alpha$-RuCl$_3$, a leading candidate material for realizing a Kitaev quantum spin liquid, to investigate its electronic structure through optical spectra. AI Theorist develops a new interpretation of the optical and photocurrent observations, identifying distinct excitonic states with contrasting optical selection rules and real-space distributions. To our knowledge, this is the first demonstration of an AI system autonomously developing a physical model to explain previously unpublished experimental observations in a quantum material, utilizing first-principles electronic-structure and many-body calculations. Our results establish a route to autonomous theoretical discovery in materials science, in which AI agents use first-principles calculations to turn experimental observations into physical models and testable predictions.

---


### 36. [An AI-Based Multi-Stage Approach for Androgenetic Alopecia Assessment from Low-Magnification Scalp Images](https://arxiv.org/abs/2610.02421)

**<font color=#1a73e8>作者：</font>** Mahmoud Raslan, Nada Omar, Omar Khaled 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Androgenetic alopecia (AGA) is characterized by patterned follicular miniaturization, increased single-hair follicular units, and altered hair-shaft diameter. We present an automated quantitative scalp-analysis and clinical decision-support framework combining FU localization, ordinal visible-shaft counting, calibrated shaft-width estimation, regional aggregation, and an interpretable rule layer. The clinical cohort comprised 243 patients (127 AGA, 116 non-AGA), while the computer-vision experiments used 160 expert-annotated patients, 2,400 trichoscopic images, and approximately 158,000 FU annotations. Under patientdisjoint evaluation, YOLOv8m achieved test mAP@0.5=0.920 and recall=0.860; EfficientNet-B5 with a support-map channel achieved 87.0% expert-box count accuracy (macro F1=0.85). A separate 500-image set was processed end-to-end with detector-generated boxes, yielding MAE of 6.56 for follicle detection and 16.59 for follicle classification relative to human-expert annotations. The system is intended to assist, rather than replace, dermatologist interpretation.

---


### 37. [Geometry-Aware Time Reparameterization for Flow-Map Distillation](https://arxiv.org/abs/2610.02427)

**<font color=#1a73e8>作者：</font>** Félix Dedek, Makoto Yamada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-map distillation enables one- and few-step generation by learning finite-time transitions of a pretrained generative ODE. We investigate whether changing the teacher's time parameterization can make these transitions easier to learn. Motivated by the hypothesis that trajectory segments with large normal acceleration are harder to distill, we propose a geometry-aware time reparameterization that allocates more student time to these regions while preserving the teacher's geometric paths and terminal distribution. We derive a shared clock that equalizes a population normal-acceleration statistic under suitable assumptions, and construct a practical approximation from robust, regularized estimates across teacher trajectories. We incorporate this clock into Lagrangian flow-map distillation, using the transformed time coordinate to condition the student. The clock is estimated once before distillation and requires neither teacher retraining nor additional student parameters or inference-time network evaluations. Experiments on synthetic data, CIFAR-10, and CelebA-64 show improved sample quality over identity-time distillation at matched inference budgets, including improvements in one- and two-step image generation. The gains in one-step generation, where no intermediate sampling times can be adjusted, highlight the benefits of time reparameterization during distillation.

---


### 38. [CRISP: A Framework for Clause-Reconstructed Interpretable NeuroSymbolic Propositions](https://arxiv.org/abs/2610.02431)

**<font color=#1a73e8>作者：</font>** Alex Chan, Shafi Muhtasim Chowdhury, Ekin Can Erkuş 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks achieve high accuracy through layered numerical transformations, yet their decisions remain difficult to audit because decision evidence is encoded in hidden activations rather than explicit rules. This paper introduces CRISP, a framework that reconstructs the last-layer activation vector (LLAV) of binary neural teachers as Tsetlin Machine (TM) clauses. CRISP sign-binarizes the teacher's penultimate pre-logit activations, and assigns one Individual TM (ITM) to each LLAV neuron. Each reconstructed hidden bit is represented by propositional clauses over Booleanized input features, which gives a direct symbolic trace from named input thresholds to a named teacher neuron. CRISP is evaluated on MNIST, KMNIST, FashionMNIST (FMNIST), SVHN, and CIFAR10 using a BinaryConnect convolutional neural network (BCCNN) teacher and a fully binary neural network (BNN) teacher, with an additional study on binary thresholding, thermometer encoding, and quartile binning at multiple bit depths. The results show that LLAV sign-binarization does not reduce teacher-head accuracy in the tested BNN setting, while ITM reconstruction error is the main limiting factor. Quartile one-bit Booleanization gives the strongest reconstruction fidelity on SVHN at 87.52% test fidelity and is competitive on CIFAR10, and the reconstructed LLAV preserves 78.41% teacher-head accuracy on FMNIST. Pooled clause-evidence visualizations show that the learned ITM literals concentrate on the object region in centered benchmarks. CRISP therefore provides a clause-level route for inspecting the final hidden representation of binary neural teachers.

---


### 39. [SoK: Stablecoins in the Quantum Era](https://arxiv.org/abs/2610.02435)

**<font color=#1a73e8>作者：</font>** Panagiotis Chatzigiannis, Navid Alamati, Suvradip Chakraborty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Stablecoins support payments, trading, collateral, and cross-chain settlement across the digital-asset ecosystem. They also concentrate value behind issuer, custody, upgrade, oracle, and bridge keys while inheriting the quantum vulnerabilities of host-chain accounts, consensus, rollups, and privacy systems. This paper presents a Systematization of Knowledge (SoK) on post-quantum stablecoins. We develop a stablecoin-specific threat model, map cryptographic dependencies to monetary control surfaces, and classify migration choices along three dimensions: who can authorize a change, where the change must occur, and whether it is hybrid, post-quantum native, or an encapsulation of a classical component. We emphasize an authority-liability gap: the party able to migrate a component is often different from the holders, exchanges, protocols, or issuers that bear the loss if it fails. We review the relevant cryptographic primitives, but distinguish general blockchain failures from their stablecoin-specific effects. We also examine recent blockchain and issuer-controlled interoperability proposals, and relate migration choices to redemption, continuity, and intervention requirements under current stablecoin regulation. Our findings identify open problems in aggregate and threshold authorization, operation-specific security levels and costs, dormant and wrapped supply, private and compliance-enabled transfers, and measurement of quantum-vulnerable stablecoin exposure.

---


### 40. [A Generative Model of Complex Networks Using Graphons and Neural Inverse Operators](https://arxiv.org/abs/2610.02439)

**<font color=#1a73e8>作者：</font>** Wooseong Choi, Italo'Ivo Lima Dias Pinto, Chen Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative graph models are central to understanding and simulating complex networks. However, existing approaches have complementary strengths and limitations. Mechanistic models offer interpretability but rely on instance-specific estimation methods. Deep generative models, on the other hand, offer amortized inference at the cost of interpretability and are largely limited to graph sizes seen during training. Scientific applications motivate a framework that retains the strengths of both paradigms. We bridge them by formulating both the generative model and parameter recovery in function space. A multifractal step graphon extends standard step graphons with a recursive construction that compactly parameterizes complex networks. This formulation admits a neural inverse operator to recover its parameters, enabling inference on unseen graph sizes. We evaluate our model, trained only on synthetic multifractal step graphon realizations, against both paradigms. Against a graph foundation model pretrained on empirical networks, our method achieves the best average performance on three of four metrics in a zero-shot graph-generation benchmark, indicating that the model transfers to real-world graphs. We also apply our method to single-observation networks, a regime largely inaccessible to deep models that require training corpora, where it performs comparably to an instance-specific method that optimizes on each graph. In a multi-subject EEG case study, the inferred parameters track a reversible change in brain state more sensitively than traditional network statistics. Together, these results indicate that mechanistic interpretability and amortized inference can be effectively unified in a generative graph model to enhance our understanding of complex networks.

---


### 41. [Bandits via Additive Quantized Representations](https://arxiv.org/abs/2610.02440)

**<font color=#1a73e8>作者：</font>** Ami Tavory, Noam Touitou, Tal Sarig 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual bandits require balancing nonlinear reward modeling with online efficiency. Tree ensembles and neural methods capture nonlinearities but require periodic retraining and large replay buffers. Linear models update efficiently per observation with O(1) memory, but are fundamentally restricted to linear reward structures. We propose Residual Quantization (RQ) as a representation layer to bridge this gap. An offline-trained RQ codebook maps continuous contexts into discrete centroid assignments across multiple levels, set dynamically through a shadow mechanism. This enables a spectrum of additive bandit algorithms that achieve nonlinear expressivity with strictly bounded memory. Across 13 datasets, RQ variants beat their non-RQ counterparts on 11 of 13 datasets, often by wide margins, while matching doubling-retrain XGBoost and neural baselines using up to 1000 times less memory.

---


### 42. [Reinforcement Learning Techniques for the Optimization of Target Polarization in Nuclear Physics Scattering Experiments](https://arxiv.org/abs/2610.02452)

**<font color=#1a73e8>作者：</font>** Armen Kasparian, Torri Jeske, Monibor Rahman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The operation of dynamically polarized targets in nuclear physics experiments relies on continuous tuning of the microwave frequency to compensate for radiation damage and evolving material properties, a task that is traditionally performed through manual trial-and-error by expert operators. This work presents a data-driven control framework that combines surrogate modeling with reinforcement learning to optimize the target polarization. Using operational data from the APOLLO cryogenic target system, we train and evaluate multilayer perceptron and Gaussian process regression models to predict polarization as a function of microwave frequency, beam current, and accumulated radiation dose. We show that Gaussian process-based models provide calibrated uncertainty estimates and reliably identify regions outside the training distribution, while MLPs exhibit limited sensitivity to distributional shift. To enable learning and control across multiple target samples, we introduce a Gaussian process approximation and embed the surrogate model within a standardized simulation environment. A reinforcement learning agent is trained using a lower-confidence-bound reward formulation that balances performance maximization against uncertainty. We are able to show an almost 2x improvement on the operators actions utilizing our RL agent.

---


### 43. [A Composable AI-Accelerated Iterative Solver for 3D-IC Thermal Modeling](https://arxiv.org/abs/2610.02461)

**<font color=#1a73e8>作者：</font>** Yixing Li, Jiahang Zhou, Zhiyu Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate thermal analysis of heterogeneous 2.5D/3D-IC packages is essential yet computationally prohibitive. A single full-package FEM simulation can take hours, while AI-based surrogates treat the entire stack as a monolithic prediction target and must be retrained whenever the die count or topology changes. To address this limitation, this work proposes Domain-Decomposed AI-Accelerated Iterative Solver for Thermal Analysis (DAIST), a composable thermal solver that decomposes the global package simulation into block-level subdomain problems, replaces subdomain solvers with neural operators, and couples them through iterative exchanges of interfacial temperature and heat flux. This local-to-global architecture eliminates the topology lock-in of monolithic models: block-level neural operators can be directly reused in unseen package assemblies without retraining. The iterative coupling strategy further provides a controllable accuracy-runtime tradeoff, where the iteration budget can be adjusted to trade accuracy for runtime. Evaluated on a multi-chiplet system and an advanced packaging system, DAIST achieves up to $178\times$ speedup over traditional FEM solvers with mean temperature errors of 0.068% and 0.323%, respectively, while demonstrating cross-topology reuse of block-level models across structurally distinct package assemblies.

---


### 44. [From Retrieval to Typed Decisions: Calibrated System One Models from Biomedical Sentence Encoders](https://arxiv.org/abs/2610.02486)

**<font color=#1a73e8>作者：</font>** Pritam Deka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typed decision models answer schema-constrained questions about a text in one forward pass and return probabilities meant to be thresholded. We ask whether biomedical sentence encoders trained for retrieval are good starting points for such models. We present SBERT2S1, which converts Sentence-Transformers encoders into bi-encoder, cross-head (C) and prior-fused residual (PFR) decision models, together with BIODECIDE, a biomedical typed-decision suite, and MEDLINE-S1, 243k training decisions derived from NLM indexing. Across six parent-retriever pairs, retrieval training improves zero-shot matching of content-bearing options. After fine-tuning, its effect depends on the head: across five pairs and three training-set sizes, retrieval training significantly helps PFR, which keeps the retrieval prior, in 10 of 15 comparisons, but helps C in one and hurts it in five. A matched grid of two heads and five training objectives shows that C outperforms PFR under every objective, and that the released RLCD recipe of open System One models trails cross-entropy by 2.5-3.0 points. The deficit stems mainly from its reward normalisation, which inflates the noisy score-function term 3.6-15-fold; an unbiased leave-one-out estimator recovers most of the gap. After temperature scaling, no objective is clearly better calibrated than cross-entropy. We release the code, the MEDLINE-S1 labels and a model.

---


### 45. [Threshold-Aware Conformal Routing](https://arxiv.org/abs/2610.02487)

**<font color=#1a73e8>作者：</font>** Shiwei Tan, Huzefa Rangwala, Danielle C. Maddix  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-fidelity simulations are essential to scientific and engineering design, but can be expensive to run repeatedly. Learned surrogates offer a faster alternative, yet their higher errors may alter downstream decisions. This accuracy-speed tradeoff creates a need to determine whether a surrogate can be used or the full simulator remains necessary. We study decisions determined by whether a scalar quantity of interest lies above or below a fixed threshold. For each input, we use the surrogate when its conformal interval lies entirely on one side of the threshold and route the input to simulation when the interval intersects it. Standard conformal prediction constructs intervals without reference to the downstream decision threshold: even a narrow interval near the threshold can cross it and trigger simulation, whereas a wider interval farther away can remain entirely on one side and require no simulation. We introduce Threshold-Aware Conformal Routing (TACR), which learns an input-dependent scale using a threshold-aware objective that concentrates interval tightness near the decision boundary. Exact split-conformal calibration on held-out data preserves distribution-free marginal coverage, which also upper-bounds the probability of an incorrect threshold decision that is not routed. Across various scientific and engineering datasets, TACR reduces simulator deferrals by 14-75% relative to standard conformal prediction at the same coverage target. Against a variant without threshold-local weighting but with similar predictor accuracy, TACR further reduces deferrals by 10-24% on four datasets. These results show that optimizing interval allocation for routing can reduce simulator calls without weakening the standard conformal guarantee.

---


### 46. [DeepStratNet: A Context-Aware Coordinate Regression Framework for Seismic Horizon Tracking under Sparse Labels](https://arxiv.org/abs/2610.02494)

**<font color=#1a73e8>作者：</font>** Aniq Ahmad, Musham Ahmad Malik, Ahmad Mustafa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic horizon tracking is a foundational task in 3D seismic interpretation. Most existing deep learning approaches formulate it as dense semantic segmentation, typically using U-Net-based architectures. The model produces a probability map over all pixels that must be post-processed to extract precise horizon coordinates, while horizon picks in time/depth must be converted into dense masks for training. Unpicked seismic traces are consequently treated as background, which can hinder convergence, and both pre- and post-processing can introduce errors into the final interpretation. Moreover, 2D segmentation models do not inherently capture inter-slice context, while 3D models are often computationally prohibitive. We instead formulate horizon tracking as a bounded coordinate regression problem, where the model directly predicts the time/depth coordinate of the target horizon at each lateral position. We propose a lightweight regression head compatible with any pretrained vision backbone, coupled with an LSTM module to model inter-slice context and produce a continuous horizon surface across the volume. A combination of L1 and L2 losses supervises predictions at valid horizon picks, while a geology-informed regularization enforces lateral continuity between successive traces. Under controlled experimental conditions, we evaluate four pretrained vision backbones under both segmentation and regression configurations on a seismic volume from New Zealand. The proposed approach consistently outperforms its segmentation counterparts quantitatively, using metrics including RMSE and PCC, and qualitatively, while also demonstrating greater robustness to increasing sparsity of training picks. Finally, we show that prediction variation across successive traces captures local variations in geological complexity, providing an automated quality control measure for downstream seismic interpretation.

---


### 47. ["I just assumed that it would translate": examining MT risk awareness among healthcare staff with abbreviations as a use case](https://arxiv.org/abs/2610.02496)

**<font color=#1a73e8>作者：</font>** Eleanor Taylor-Stilgoe, Félix do Carmo, Constantin Orăsan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the UK, public healthcare staff report turning to machine translation (MT) - predominantly Google Translate (GT) - to communicate with patients across language barriers. Though intended to support their duty of care, potentially uninformed reliance on MT in such contexts could have serious consequences for patient safety. Research nonetheless remains limited on staff awareness of the possible risks posed by higher-stakes MT use in general and with patient medical records in particular, most existing literature instead examining its use in interpersonal situations or with patient-oriented documentation. Moreover, medical abbreviations are well-documented as increasing patient risk even monolingually, with outcomes from their misuse and/or misinterpretation ranging from temporary harm to the death of the patient. Abbreviations were therefore selected as a use case for identifying the potential risks posed by their translation with MT. Contextualised French and Spanish data examples drawn from authoritative clinical corpora and translated via GT were presented during semi-structured interviews to 21 healthcare staff participants in diverse roles and specialties. The results were then subject to qualitative analysis and cross-analysis.

---


### 48. [HXAI: Hierarchical Privacy-Preserving Explainable AI in Distributed Energy Systems](https://arxiv.org/abs/2610.02504)

**<font color=#1a73e8>作者：</font>** Poushali Sengupta, Sabita Maharjan, Frank Eliassen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Balancing electricity demand and supply is increasingly difficult due to the inherent intermittency of renewable power generation and the stochastic power consumption. Grid operators require fine-grained, decision-relevant insights into household energy consumption to manage peak loads and design responsive tariffs, but increased transparency at this level raises significant privacy concerns. Traditional methods for explainable AI (XAI) can reveal sensitive information, while standard privacy techniques often reduce the usefulness of explanations. To address this issue, we introduce HXAI, a hierarchical framework that preserves privacy while enabling reasonable explainable analysis for grid-level demand management. HXAI consists of two main components: (1) a local model that generates fine-grained explanations within a secure, private environment, and (2) a zonal model that aggregates these explanations to support grid-level analysis while enforcing privacy through flexible privacy-budget management. We explicitly limit cumulative privacy exposure under repeated operator queries and show that the proposed framework preserves decision-relevant information without compromising household privacy. Experiments on both simulated and real-world energy datasets demonstrate that HXAI provides useful insights for zonal load management while ensuring that appliance-level consumption remains local and is never transmitted to grid operators. Our results show that preserving the semantic structure of explanations, rather than minimizing numerical error, is the key to XAI under differential privacy. This framework provides a way to achieve both privacy and explainability in energy management.

---


### 49. [Multi-Fidelity Policy Gradients Stabilize Data-Scarce Reinforcement Learning](https://arxiv.org/abs/2610.02505)

**<font color=#1a73e8>作者：</font>** Xinjie Liu, Ruihan Zhao, Anirban Chaudhuri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy gradient methods for on-policy reinforcement learning (RL) can become unstable when expensive, scarce target-domain data yield noisy gradient estimates. We address this challenge by complementing limited high-fidelity (HF) target-domain data with abundant, cheap, but biased low-fidelity (LF) data, e.g., from a simplified simulator. Most existing methods directly optimize biased objectives based on LF data. In contrast, the recently introduced multi-fidelity policy gradient (MFPG) framework uses LF data solely to construct a control variate that reduces variance and improves HF data efficiency without biasing the policy gradient estimator. However, published work on MFPG is limited to REINFORCE on small-scale simulation tasks. We develop MFPG for modern actor-critic learning in GPU-parallel simulation and on a physical robot. Our analysis and experiments show that naive extensions to proximal policy optimization (PPO) can lose cross-fidelity correlation or inflate variance. Our MFPG-PPO addresses these failures by redesigning the sampling, advantage estimation, and control variate construction to preserve cross-fidelity correlation, and by monitoring estimator uncertainty to prevent variance inflation. We also introduce a budget-aware MFPG-PPO to divide a fixed sampling budget among high- and low-fidelity data sources. Across simulated robot locomotion tasks of varying LF-to-HF transfer difficulty and HF data budgets, MFPG-PPO improves upon PPO trained on HF data alone in nearly all settings, and consistently matches the performance of PPO trained with 16x more HF data on the hardest task at the smallest HF budgets. In contrast, most baselines that use LF data perform well only where direct LF-to-HF transfer succeeds. MFPG-PPO enables stable learning on a physical Franka arm using only 4 real-robot episodes per update and no human demonstrations.

---


### 50. [World Action Modeling with Progressive Visual Planning](https://arxiv.org/abs/2610.02508)

**<font color=#1a73e8>作者：</font>** Fei Zhang, Zhaochong An, Duncan Frost 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) have emerged as a promising paradigm for robotic control by jointly predicting future visual dynamics and actions from an initial observation and instruction. However, existing WAMs struggle with long-horizon prediction, as generating dense video rollouts is highly inefficient. Some recent WAMs address this by predicting a single future frame without generating the full video, but this approach neglects how to progress toward the goal. We present ProWAM, a progressive world action model that jointly predicts actions and an ordered sequence of sparse visual sub-goals, providing explicit visual guidance to anchor action generation throughout task execution. This design scales naturally, as sub-goal prediction can be learned from large-scale action-free videos, allowing the video backbone to offload complex visual planning from the action policy. For efficient action generation, ProWAM executes a single video-backbone forward pass to cache sparse sub-goal features, eliminating iterative full-video generation and requiring only lightweight action denoising during replanning. Across extensive evaluations, ProWAM achieves superior out-of-distribution robustness. On simulation benchmarks, it sets new state-of-the-art results on LIBERO-Plus (85.8%) and randomized RoboTwin (75.7%), outperforming the strongest baseline with relative gains of up to +35.9%. On RoboCasa365, ProWAM achieves a 48.1% success rate and 18.2% on the challenging Composite-Unseen split, ranking 4th overall. Crucially, in zero-shot real-world experiments, ProWAM achieves 70.0% success, outperforming the strongest baseline by +15.0 (from 55.0% to 70.0%, a +27.3% relative gain) in novel scenes. These results demonstrate the value of progress-indexed visual foresight for closed-loop control. Our program is in this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-260](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
