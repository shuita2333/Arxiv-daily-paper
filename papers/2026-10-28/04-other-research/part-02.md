# 📦 其他研究 | 2026年10月28日

> 本类共 **446** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-446](./part-09.md)

---

### 51. [Tree Depth and Sample-Quality-Associated Features: Two Hidden Factors in Boruta Selection for RNA-Seq Data Classification](https://arxiv.org/abs/2610.33307)

**<font color=#1a73e8>作者：</font>** Tareque Mohmud Chowdhury, Abu Raihan Mostofa Kamal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Boruta is a widely used method for selecting gene panels from RNA sequencing data, and its most used implementation recommends Random Forest trees of depth 3 to 7, an untested setting. We tested whether this setting changes which genes are selected, using pan-cancer data from The Cancer Genome Atlas (10,469 tumors, 33 cancer types) and breast cancer PAM50 subtyping (981 tumors, 5 subtypes). A leakage-free protocol fitted every label-dependent step inside training folds, measured every effect against seed-to-seed variation, and held out a locked test set per task. In pan-cancer data, shallow trees changed the selection far more than a new seed did: the top-500 overlap with unlimited-depth selections was 0.37 at depth 5, against 0.84 to 0.93 between seeds at depth 5 or unlimited depth. Shallow trees confirmed 3.5 times fewer genes, missed markers of large classes and produced less accurate 50-gene panels (balanced accuracy 0.809 vs 0.889). The effect vanished once the cap reached about 60 to 75% of the depth that unrestricted trees grow to, set mainly by the number of classes, not sample size, and leaving depth uncapped cost no accuracy in either task. The effect replicated in a second cross-validation repeat and under permutation importance. About a third of pre-filtered candidates also tracked sample quality within class; a within-class filter removed them without loss of test accuracy (balanced accuracy 0.943 vs 0.942 with 1,000 genes). We recommend uncapped trees, or a cap chosen from the realized tree depth, and a within-class quality filter before Boruta.

---


### 52. [MLIPDiff: Guiding Denoising Diffusion Models for Structure-Based Drug Design via Machine-Learned Interatomic Potentials](https://arxiv.org/abs/2610.33315)

**<font color=#1a73e8>作者：</font>** Yiyan Liao, Amin Tavakoli, Yu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become a dominant approach to structure-based drug design. However, because they are trained primarily to fit reference structures, they often place ligands in physically implausible poses that clash with the protein. We introduce MLIPDiff, an inference-time guidance method that can be applied to pretrained diffusion models for ligand generation. The method uses physics-informed guidance from UMA (Universal Models for Atoms), a machine-learned interatomic potential (MLIP). The guidance combines four weighted energy terms (protein-ligand interaction, ligand strain, steric clash, and pocket anchoring) and uses the original model checkpoint without retraining. On CrossDocked2020, MLIPDiff completely eliminates protein-ligand collisions while preserving the ligand's local geometry, improving bond-length distributions and physical plausibility relative to the base model. Compared to models such as NucleusDiff that are specifically designed to reduce atomic clashes, MLIPDiff achieves clash-free structures without compromising local geometry. It maintains the base model's PoseBusters pass rate and attains the best median Vina Score, Vina Min, and Vina Dock, surpassing both the base model and NucleusDiff, with a median of 59.6\% of ligands per pocket binding more strongly than the reference. MLIPDiff thus addresses a limitation of prior methods by generating physically plausible structures with favorable predicted binding affinity using a single frozen model and no additional training.

---


### 53. [AI Teaches Humans to Handle Complexity in the Game of Go](https://arxiv.org/abs/2610.33323)

**<font color=#1a73e8>作者：</font>** Adamo Cerioli, Vito D. P. Servedio, Gabriele Cerioli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Strategic decision-making in complex environments requires balancing local stability against global coordination. Using the game of Go as a bounded empirical testbed, we investigate how biological and artificial agents navigate this trade-off by formalizing a network-derived metric of strategic tension defined via the spectral radius of spatial dependency matrices. Across human skill progression, tension systematically decays from novices to masters as uncoordinated tactical skirmishes give way to disciplined territorial stabilization. However, a longitudinal analysis of professional play spanning 1980--2026 reveals a striking historical paradox: following the superhuman breakthrough of AlphaGo in 2016, elite human matches display a marked surge in sustained tension. A two-dimensional projection based on move distance and captures places modern professionals close to neural engines, separating their tension from the local contact fighting of novices and from random noise. Consequently, strategic tension acts as a macroscopic order parameter for decision paradigms rather than raw computational strength. Beyond the game of Go, these findings establish a constructive paradigm for human-AI interaction, indicating how artificial systems can act as cognitive scaffolding that expands biological heuristics and elevates human capacity to navigate higher-order complexity across professional training and decision-making domains.

---


### 54. [TempShap: When and How Much a Feature Matters in Time-Series Forecasting](https://arxiv.org/abs/2610.33330)

**<font color=#1a73e8>作者：</font>** Chi Zhao, Anastasiia Chelnokova, Jing Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Attribution for a time-series forecaster should answer two questions that a feature-level scalar cannot: when in the input window a feature acts, and how much its influence changes across the forecast horizon. Most existing Shapley explainers treat each feature as one player and therefore collapse both axes. We propose TempShap, a retrospective, loss-based Shapley framework whose players are the individual input cells $(t,i)$. Its attribution tensor yields temporal-localization and horizon-impact profiles. We validate these against planted temporal structures, a tractable exact cell game, and a closed-form attribution oracle for a real linear forecaster. Permutation sharing estimates the cell-level game at localized perturbation cost. Under redundant inputs, one-at-a-time scores under-credit substitutable information, whereas the signed Shapley decomposition preserves total value and yields more reliable held-out deletion rankings under mean masking. A planted counterexample isolates the redundancy mechanism. Experiments show a deletion-ranking advantage across Shapley estimators, forecasting benchmarks, and model families. TempShap therefore makes fine-grained Shapley attribution both practical and operationally useful.

---


### 55. [Augmentation-Guided Adversarial Training via Local Stability-Based Sample Selection](https://arxiv.org/abs/2610.33331)

**<font color=#1a73e8>作者：</font>** Daniel Agyei Asante, Mark Tetteh, Deborah Asamoah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial training remains one of the most effective defenses against adversarial attacks, but its standard PGD-based training is computationally expensive because adversarial examples are generated for every training sample. Selective adversarial training reduces this cost by perturbing only a subset of samples. However, existing selective techniques typically rely on point-wise difficulty signals such as loss, entropy, margin, or gradients. We show that these point-wise criteria do not capture local instability in a sample's neighborhood. Motivated by this, we propose Augmentation-Guided Adversarial Training (AGAT), a selective adversarial training framework that uses augmentation-induced local variation to allocate samples with unstable neighborhoods for adversarial training. AGAT ranks samples using Augmentation-based Local Stability (ALS), a lightweight score that measures the normalized change in model logits between an input and its label-preserving augmented variant. Experiments across different architectures on MNIST, CIFAR-10, CIFAR-100, and Tiny-ImageNet-200 demonstrate that AGAT achieves comparable or higher robust accuracy while applying adversarial supervision to only 20-30% of the training samples in each minibatch. AGAT also requires less training time than all other adversarial training baselines in the computational cost evaluation.

---


### 56. [Gaussian Approximation for Composition and Subsampling of Differentially Private Algorithms](https://arxiv.org/abs/2610.33333)

**<font color=#1a73e8>作者：</font>** Vitaly Feldman, Moshe Shenfeld  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The privacy analysis of differentially private stochastic gradient descent (DP-SGD) relies on bounds for the composition of subsampled mechanisms. The privacy of such a composition is bounded by that of a pair of product distributions, whose privacy loss is a sum of independent terms and has been analyzed via a variety of notions and concentration results. Yet, existing closed-form bounds either lose a logarithmic factor or require restrictive conditions on the noise scale and delicate analysis of subsampling. Further, while it is well known that sums of independent random variables are approximately Gaussian, existing CLT-based techniques give an approximation with a large error in $\delta$.
We show that the privacy loss of this pair is approximately Gaussian as long as each step has a small privacy loss except with small probability. Specifically, its privacy loss distribution is close to a Gaussian with the same mean and variance, after truncating the rare large privacy losses. The closeness in both directions is up to a shift of $\varepsilon$ that grows only as $\ln(1/\beta)$ for an additive error $\beta$ in $\delta$ and is a lower-order term in typical applications. In particular, the composition satisfies Gaussian differential privacy up to a lower-order shift of $\varepsilon$ and the additive error $\beta$. We also give a simple way to analyze the resulting variance-based bounds for subsampled mechanisms which relies on the $\chi^2$ divergence of a single step. For the Gaussian mechanism at sampling rate $1/t$ and $t>\ln^{3}(1/\delta)$, this gives the predicted rate for $\sigma\gtrsim\max\{1,\sqrt{\ln(1/\delta)}/\ln(t)\}$, whereas the standard Rényi-divergence analyses need $\sigma\gtrsim\sqrt{t\ln(1/\delta)}/\ln(t)$. We extend these results to random allocation (balls-and-bins sampling), and show that it explains the high accuracy of the connect-the-dots method.

---


### 57. [Information-Theoretic Scaling Laws for Generative Diffusion Training](https://arxiv.org/abs/2610.33337)

**<font color=#1a73e8>作者：</font>** Druv Pai, Dejan Stancevic, Yi Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models trained on increasingly large datasets sampled from the same data distribution will converge to the same learned distribution. However, in practice, a model trained on finite data depends on the particular training dataset; this dependence is reflected in properties of the model's outputs, such as memorization and sample quality. To understand this dependence through an information-theoretic lens, we study \textit{model information}, a computationally tractable measure of how much samples from the trained model depend on the particular training dataset. We explore its scaling behavior as model size and training dataset size vary. Specifically, we uncover two qualitatively distinct scaling regimes: (1) a nonlinear model information regime marking the transition from pure memorization to imperfect generalization, and (2) a generalization regime characterized by linear scaling of the model information and progressively improved generalization and sample quality. We then posit an information-theoretically principled scaling law to quantify these two regimes, and show that this law yields induced scaling laws for memorization and sample quality. We finally demonstrate that these induced scaling laws extrapolate well outside the fit's domain. Our results demonstrate information-theoretic principles for memorization and sample quality scaling laws in diffusion models. Our code is publicly available on \href{this https URL}{GitHub}.

---


### 58. [Real Time Motion Detection in Video Inspired by Photonic Time Stretch](https://arxiv.org/abs/2610.33351)

**<font color=#1a73e8>作者：</font>** Callen MacPhee, Yiming Zhou, Bahram Jalali  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion perception is fundamental to computer vision and physical AI, and plays a central role in robotics, autonomous vehicles, human-computer interaction, and video compression. Traditional approaches such as background subtraction, frame-differencing and optical flow algorithms often struggle in complex or dynamic scenes, typically sacrificing spatial resolution for computational tractability. Here we introduce MoViD (Motion estimation via Virtual dispersion and phase Detection), a physics-inspired algorithm grounded in the principles that govern photonic time stretch - a highly successful ultrafast realtime data acquisition platform. Drawing inspiration from the optical physics therein, MoViD treats video as a collection of optical time series waveforms associated with pixels. Motion of an object through a pixel broadens the time series spectrum and, after group delay dispersion, induces a temporal phase that exists only if there is motion. Spatiotemporal group delay dispersion templates, corresponding to dielectric functions, classify specific motion trajectories. Unlike conventional empirical phase-based motion-analysis pipelines that require narrow-band spatial channelization and pyramid reconstruction, the physics-based MoViD operates directly on the broadband video signal, vastly increasing its computational speed. The resulting algorithm achieves unprecedented performance in both motion characterization and motion magnification, providing full-resolution motion mapping in real time at nearly 200 frames per second at 4K resolution and 70 frames per second for 8K video - orders of magnitude faster than classical optical flow approaches or learning-based methods. Notably, such extreme performance enables real time motion analysis at ultrahigh resolution for motion detection and compensation in robotics and other autonomous devices.

---


### 59. [Detecting Temporal Concepts in Video Transformers via a No-False-Positives Test](https://arxiv.org/abs/2610.33353)

**<font color=#1a73e8>作者：</font>** Jianghuai Li, Andrew Ren, Greg Shakhnarovich  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video models have the architecture to support encoding temporal aspects of the input, i.e. concepts that require more than one frame to define, like object movement. However, because motion and appearance change are entangled, a feature that appears to encode temporal concepts like object movement may instead encode non-temporal concepts like spatial presence at different positions whose activations merely correlate with motion. To resolve this, we introduce the No-False-Positives (NFP) test, a statistical test with a formal guarantee of statistical specificity for identifying features encoding temporal concepts. Using specially designed stimuli, we apply this test to representations produced by VideoMAE, V-JEPA2, and TimeSformer, and observe that temporal features exist in each model. We validate the test first by showing it yields no temporal features for the DINOv2 image-encoder. Then, using a synthetic representation space, we show that detection rate increases with a direction's projection onto the temporal subspace, and that Sparse Autoencoder features test-flagged as temporal project much more of their norm onto the temporal subspace than unflagged features. Interventions on temporal SAE features yield mixed results across models, suggesting that intervening on temporal features may not outperform a non-temporal feature baseline.

---


### 60. [The Clustering Occupation Kernel (CLOCK) Method for Time Series Arising from Dynamical Systems](https://arxiv.org/abs/2610.33354)

**<font color=#1a73e8>作者：</font>** Michael L. Wells, Kamel Lahouel, Victor Rielly 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the Clustering Occupation Kernel (CLOCK) method, a novel representation-based framework for clustering time series arising from dynamical systems. CLOCK embeds observed sequences into a reproducing kernel Hilbert space (RKHS) via a time-averaged occupation kernel, enabling trajectory comparison through their RKHS norm. For systems governed by differential equations, this formulation rigorously approximates the kernel mean embedding of the invariant Sinai-Ruelle-Bowen (SRB) measure, meaning our dissimilarity metric approximates the maximum mean discrepancy (MMD) between attractors. To accommodate general time series, we introduce time lags via Takens' Embedding Theorem to reconstruct the phase space. Crucially, CLOCK natively handles trajectories of unequal lengths and irregularly-spaced observations. We validate the proposed metric using spectral clustering, demonstrating superior performance against benchmark methods on both synthetic datasets and a real-world intracranial large-scale electroencephalogram (EEG) dataset. Finally, ablation studies on the Lorenz-96 system are consistent with the theoretical convergence rates of the occupation kernels and highlight the method's strong robustness to zero-mean Gaussian noise.

---


### 61. [Tight Learned Event-Inertial Odometry (TLEIO): a Transformer-Based Architecture for End-to-End Motion from Event Streams](https://arxiv.org/abs/2610.33356)

**<font color=#1a73e8>作者：</font>** Matteo Cascone, David Jensen, Alessandro Pirini 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras provide microsecond temporal resolution, high dynamic range, and sparse asynchronous measurements, making them compelling for odometry under fast motion and challenging illumination. Yet, accurate event-based state estimation remains difficult: existing systems often use events as a complement to frames or rely on feature tracking, correspondence search, and optimization-heavy backends, limiting the efficiency promised by event sensing. We introduce Tight Learned Event-Inertial Odometry (TLEIO), a compact filter-based pipeline that learns short-window relative motion directly from voxelized event streams and tightly fuses the resulting constraints with IMU propagation. Its learned front-end, EventsFormer, predicts local displacements and per-axis uncertainty from event voxels in a single forward pass, while a stochastic-cloning EKF fuses these overlapping predictions with IMU propagation, producing metric trajectories without explicit feature tracks and pose optimization at inference time. The network is trained directly from pose displacements, without requiring event-flow labels. We evaluate TLEIO on the TartanAir/TartanEvent benchmark and on real DAVIS240c sequences. On TartanAir, TLEIO reduces average ATE from 2.26 m to 1.10 m over the IMU-only TLIO baseline, while achieving up to 48.9% lower runtime than optimization-based event odometry methods.

---


### 62. [Preference Optimization Improves Definition Generation: Semantic Change in EU Institutional Sustainable Finance Disclosures](https://arxiv.org/abs/2610.33357)

**<font color=#1a73e8>作者：</font>** Mariia Fedorova, Andrey Kutuzov, Gustavo Cadenas Delascio  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dictionary-like definition generators are known to be useful for lexical semantic change detection (LSCD). However, they suffer from overly granular sense distribution, producing excessive number of definitions for one and the same lexical sense. In this work, we show that fine-tuning with Direct Preference Optimization (DPO) helps to overcome this problem. We test our approach both quantitatively on a curated academic LSCD benchmark and qualitatively on real-world data for a practical task of auditing diachronic changes in sustainability terminology within project documentation of EU development finance. All models, code and predictions produced in this study are publicly available at this https URL.

---


### 63. [The Cost of an Unknown Horizon for the Last Iterate of Clipped SGD under Heavy-Tailed Noise](https://arxiv.org/abs/2610.33381)

**<font color=#1a73e8>作者：</font>** Yuxing Peng, Zhiqing Tang, Weijia Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training is often stopped at a data-dependent time, as in early stopping, and the last iterate is kept. Guarantees valid at such times must hold at all times simultaneously. We determine the optimal time-uniform rate for the last iterate of clipped SGD on smooth convex objectives under heavy-tailed noise with a bounded central $p$th moment, $1<p\le2$. A schedule without horizon or confidence inputs attains $\tilde O(t^{-\beta_p})$ at all times, with $\beta_p=2(p-1)/(3p-1)$, also almost surely, and no rule that steps along the stochastic gradient at its current iterate attains $\tilde O(t^{-r})$ for any $r>\beta_p$, even with adaptive step sizes and thresholds. This rate lies between the optimal rate $O(T^{-\alpha_p})$ for a known horizon $T$, $\alpha_p=(p-1)/p$, and the previous time-uniform rate $\tilde O(t^{-2(p-1)/(3p)})$ (Chezhegov et al., ICLR 2026); under finite variance, the exponents are $1/2$, $2/5$, and $1/3$. Their conjecture that a better schedule reaches the optimal rate thus holds with a known horizon, as shown by Liu and by Jiang et al., but fails without one. Querying gradients at the running average of the iterates attains $\tilde O(t^{-\alpha_p})$ at all times, whereas heavy-ball momentum with geometric forgetting and polynomially bounded steps cannot improve on $\beta_p$.

---


### 64. [Rethinking Microscopy Generation: Co-Designed Diffusion for Biologically Interpretable Single-Cell Synthesis](https://arxiv.org/abs/2610.33398)

**<font color=#1a73e8>作者：</font>** Shumpei Takezaki, Duway Nicolas Lesmes-Leon, Ryoma Bise 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models for microscopy can already produce realistic whole-image fields of view, but offer no principled way to control how each individual cell looks. We address this gap by recasting microscopy generation at the single-cell level and designing the input controls and the model's internal representation jointly, so that both are organized along the same biologically meaningful directions. On the input side, we aggregate a long list of standard cell measurements into a small set of semantic axes (size, elongation, brightness, texture, etc.) that are each named, measurable, and traversable. On the model side, we introduce BioVAE, an encoder-decoder whose latent space is explicitly aligned with the same set of measurements. A key finding is that the benefit of biologically structuring the latent emerges only when conditioning is also moved to the semantic axes, showing that the two ends must be designed jointly. Experiments on LIVECell show that semantic-axis conditioning substantially improves generative fidelity over high-dimensional conditioning, a blind study with biologists confirms the realism of generated cells, and per-axis traversals produce stable and interpretable phenotypic changes.

---


### 65. [From Caveman to COBA: Coordinated Optimization-Based Attacks on Grid-Edge Smart Inverters in DER-Rich Power Systems](https://arxiv.org/abs/2610.33401)

**<font color=#1a73e8>作者：</font>** Emad Abukhousa, Anna Raymaker, Animesh Chhotaray 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Aggregation platforms and smart-inverter control channels can allow a compromised coordination layer to alter active- and reactive-power commands across a geographically distributed DER fleet. This paper introduces the Coordinated Optimization-Based Attack (COBA), which uses network information and location-specific DER P/Q setpoints to maximize thermal loading on a selected transmission corridor. COBA is compared with low-information CAV baselines limited to a single uniform fleet command: all-off, all-on, maximum reactive absorption, or maximum reactive injection. The Hawaii Synthetic Grid-37 Buses case is evaluated with rooftop-photovoltaic-like capability aggregated at 20 selected 69-kV buses and verified using MATPOWER power flow. Under the case's single-reference-bus balancing convention, COBA overloads B86 (WAIALUA69-WAIANAE69) near 30% penetration and B51 (COCONUT69-PALM69) near 55%, while same-target uniform loadings remain lower and uniform commands primarily stress other natural weak lines. The results show that topology, target selection, and command capability determine DER-induced thermal risk beyond aggregate penetration alone.

---


### 66. [Bidirectional Cross-frequency Domain Interaction Network for UHD Low-Light Image Enhancement](https://arxiv.org/abs/2610.33402)

**<font color=#1a73e8>作者：</font>** Bo Fu, Hai Chi, Liyan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Ultra-High-Definition (UHD) low-light image enhancement (LLIE) methods typically rely on either spatial- or frequency-domain modeling, or independently process different frequency components for efficient restoration. However, they often fail to jointly exploit complementary spatial--frequency information and the inherent relationship between illumination and structural information across frequencies, leading to inconsistent illumination, residual noise, and detail artifacts. In this paper, we propose a novel Bidirectional Cross-frequency Domain Interaction Network (BiFreqNet) for UHD LLIE. Specifically, BiFreqNet incorporates a Dual-domain Feature Interaction (DFI) module into the multi-scale representations of a pretrained variational autoencoder (VAE) to perform reciprocal enhancement between low- and high-frequency features. DFI consists of a Spatial and Spectral-Aware Low-Frequency Enhancement (S$^2$LFE) block and a Cross-Frequency Enhancement (CFE) block. S$^2$LFE exploits high-frequency structural cues to guide low-frequency restoration and jointly models spatial and spectral information to recover global exposure and spatially varying illumination while suppressing sensor noise. CFE further leverages the enhanced low-frequency contextual information to guide adaptive high-frequency refinement, enabling faithful reconstruction of structures and fine details. Extensive experiments on four general and UHD LLIE benchmarks demonstrate that BiFreqNet achieves competitive or superior performance compared with state-of-the-art methods.

---


### 67. [Faithful Federated Tabular Data Synthesis](https://arxiv.org/abs/2610.33403)

**<font color=#1a73e8>作者：</font>** Zilong Cao, Hai Zhang, Xuan Bi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data is an important data source in the AI era. This paper studies the generation of mixed-type tabular synthetic data in federated settings, where two key challenges arise: ensuring distributional fidelity and effectively handling mixed-type data. We propose Federated Integrative Two-Step Synthesis (FITS), a framework for mixed-type tabular data synthesis. At its core is a two-step federated algorithm for estimating conditional cumulative distribution functions (CDFs) using local linear regression. Building on this algorithm, we develop a federated synthesis procedure based on the probability chain rule to ensure distributional fidelity. To handle mixed-type data, FITS introduces a continualization method that lifts discrete variables into a continuous space and recovers their discrete distributions without loss at both the density-function and CDF levels. This transformation provides a unified continuous representation of mixed-type variables, facilitating the application of local linear regression and synthetic data generation. Our theoretical analysis characterizes the conditional density and cumulative distribution functions of the continualized mixed-type variables and establishes the uniform convergence of the resulting federated conditional CDF estimators. Experiments demonstrate that FITS-generated synthetic data improves downstream task performance for all clients, with the benefits depending on how the synthetic data is used.

---


### 68. [Benchmarking System One Models for Time-Series Decision Making: A Case Study of Jev](https://arxiv.org/abs/2610.33410)

**<font color=#1a73e8>作者：</font>** Jianye Wang, Kexin Zhang, Jiayin Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time-series tasks require both accurate predictions and fast decisions. Advances in large models have introduced decision-oriented models that directly output answers and their probabilities, which we call Structured System 1 models. Their applicability to time-series tasks remains underexplored. Using Jev 1.13.0 as a case study, we evaluate time-series classification, event type prediction, oil temperature direction and stock movement prediction, converting continuous forecasting targets into discrete decisions to fit the model interface. We establish a unified evaluation framework using accuracy and AUC. Results show stronger performance on selected explicit temporal patterns and event type prediction, but near-chance discrimination on many numerical sequence classification tasks and stock movement prediction. Some datasets also reveal a gap between ranking quality and final decision accuracy. These findings motivate improvements in temporal representation, domain adaptation, and decision-score alignment. Standardized sample construction, model calls, and result recording support extending the evaluation to future models.

---


### 69. [Performance Gaps Between Open-Loop, Certainty-Equivalent, and Optimal Control Under Action-Dependent Observations](https://arxiv.org/abs/2610.33412)

**<font color=#1a73e8>作者：</font>** Leo Maynard-Zhang, Sunmook Choi, Yahya Sattar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In dynamical systems, feedback can improve performance by allowing decisions to depend on past observations, rather than being designed a priori. Under full observation, the current state is sufficient for decision-making; under partial observation, the controller must instead estimate the state from measurements. When actions also affect observations, control can have a dual role: actions influence both the state and the information available for future decisions. This interaction can invalidate certainty-equivalent (CE) control, a widely used strategy that applies state feedback policies as if the estimated state were the true state. We ask when this suboptimality leads to a quantitative performance gap that grows with the horizon. We study this question in a linear-quadratic system with bilinear observations by comparing the optimal policy, certainty-equivalent control, and the optimal open-loop (OL) policy. We identify an instance-dependent information-strength parameter $q$ and establish distinct performance regimes as $q$ varies. When $q$ is sufficiently small, we show that no policy can improve over OL control by more than $O(1)$ cumulative cost. For large values of $q$, we find that CE achieves an $\Omega(T)$ advantage over OL control. Our main finding is that for intermediate values of $q$, we can construct a policy that occasionally probes for information and achieves an $\Omega(T)$ advantage over OL control while CE only achieves an $O(1)$ advantage, establishing an $\Omega(T)$ gap between CE and optimal control. Our analysis relies on a regret decomposition that captures the tradeoff between the immediate cost of gathering information and its future benefit.

---


### 70. [How Robust Are CNNs and Vision Transformers for Alzheimer's MRI Classification Across Datasets?](https://arxiv.org/abs/2610.33416)

**<font color=#1a73e8>作者：</font>** Hafija Aktar, Molly Croes, Frank S. Menniti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate assessment of Alzheimer's disease stages from MRI is important for understanding disease progression and supporting the development of computer-aided analysis tools. Deep learning models have shown promising results for Alzheimer's disease classification from MRI. However, when evaluated on single datasets, it is difficult to determine whether the observed performance reflects consistent architectural behavior or dataset-specific effects. In this work, we present a multi-dataset benchmarking framework with standardized preprocessing and evaluation. We compare five architectures: ResNet-50, ReXNet-150, Swin Transformer, ViT-Base, and ViT-Large. The models are evaluated across three MRI datasets representing severe class imbalance, train-test distribution mismatch, and large-scale augmentation. The results show broadly consistent performance patterns across datasets, with ViT-Large achieving the best performance on all three datasets and reaching up to 99.84% accuracy and 99.86% macro F1. Performance differences between architectures are most pronounced under distribution mismatch and considerably smaller in the augmented-data setting. Across datasets, lower class-level performance is observed primarily among adjacent early-stage categories, particularly Very Mild and Mild impairment. These findings highlight the importance of evaluating deep learning architectures across multiple data conditions rather than relying on single-dataset performance.

---


### 71. [An Empirical Study of Reinforcement Learning Scaling Laws](https://arxiv.org/abs/2610.33420)

**<font color=#1a73e8>作者：</font>** Zeyu Zheng, Clare Lyle, Khimya Khetarpal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The discovery of scaling laws enables prediction of the performance, the optimal resource allocation strategy, and the best hyperparameter configuration of a large-scale training job based on inexpensive experiments at smaller scales. Guided by these empirical scaling laws, the deep learning community has achieved great success in training large (self-)supervised models on Internet-scale datasets. In contrast, despite its potential and wide application, reinforcement learning (RL) has yet to find a guiding principle for predictable scaling. In this work, we conduct an empirical study of RL scaling laws of an actor-critic algorithm in two procedurally generated environments, Starpilot and Craftax. We discover empirical scaling laws with strong predictive performance in both environments. The discovered scaling laws accurately predict the aforementioned three quantities for larger-scale training jobs up to two orders of magnitude in total training compute. In particular, we employ a variant of Elo scores for the single-agent RL paradigm as an alternative performance metric than the commonly used mean episode return. Our results show that the Elo score is a much more predictable metric than the mean episode return, making it a better choice for fitting scaling laws. By applying our discovered scaling laws to increase training compute, we establish a new state of the art in the challenging Craftax environment. Beneath the surface of the global scaling trend, we also observe a non-monotonic scaling pattern of the compute-optimal model size in Craftax. We connect this observation to a pathology known as Ray interference.

---


### 72. [Exact Unlearning After Data Curation](https://arxiv.org/abs/2610.33426)

**<font color=#1a73e8>作者：</font>** Priyank Jayraj, Devanshu sahoo, Uday Mittal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training pipelines often remove similar examples before fitting a model. Deleting a raw record can change that selection and admit an example that was excluded before. What must a service retain to reproduce training after such requests? We answer this question for a fixed rule in which earlier similar records block later ones. A limit on the total number of future deletions identifies exactly which records can still enter training. We use this boundary to build a summary of training statistics that can be repaired exactly after repeated deletions. The repaired summary is the same as rebuilding it on the surviving data with the remaining budget. We also construct finite-precision features for ridge regression, a linear learner with a penalty on coefficient size. With exact rational outputs, allowing one more deletion changes the required private information. It rises from zero to every private feature sign in the excluded candidates. An encoding attains this conditional private-information minimum on the constructed family throughout a sequence of requests. On 1,001 AskUbuntu development records, deleting an initially excluded record admits another record at 13 of 51 fixed similarity cutoffs. Exact membership repair passes 13,056 deletion-step checks. Two model-based semantic calibrations fail their fixed criteria, so the downstream task study is not run. The central result is a retention contract: the future deletions a service promises to support determine which excluded data can still be needed.

---


### 73. [Dynamic Query as Budgeting for Tiny Object Detection](https://arxiv.org/abs/2610.33430)

**<font color=#1a73e8>作者：</font>** Yi Zhang, Di Xiong, Ge Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent DETR-based tiny object detectors adopt dynamic query mechanisms to handle severe density imbalance. However, existing designs entangle two effects: how many and which queries are decoded. This entanglement obscures what drives the gains and complicates dynamic-query design; additional learned predictors and heuristic filtering also introduce overhead and potential selection errors. We disentangle these effects and show that dynamic query primarily acts as \emph{budgeting}---allocating decoder query capacity according to object density---rather than intricate query this http URL by this view, we formulate a monotonic and conservative budgeting principle and propose a budgeting-based DETR (BUTR), a streamlined framework that uses a lightweight, non-learned budgeter to estimate an input-dependent query budget $K(x)$ from encoder confidences. BUTR retains standard Top-$K(x)$ query initialization without additional learned modules or heuristic filtering in the this http URL $800\times800$ resolution, BUTR-L achieves 35.7 AP at 47.8 FPS on AI-TOD-v2 and 29.8 AP at 42.1 FPS on VisDrone on an NVIDIA T4 GPU. Inference-time integration on COCO further demonstrates its applicability to general scenario detection. Code is available at this https URL.

---


### 74. [Combinatorial Lock for Trojan-Resilient AI Engines via Hash-Assisted Spectral Filtering](https://arxiv.org/abs/2610.33437)

**<font color=#1a73e8>作者：</font>** Soumita Chatterjee, Sudip Ghosh, Tamal Ghosh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-trigger backdoor attacks, in which heterogeneous trigger mechanisms (e.g., patch, blend, warping, and the latent-domain Spy-Watermark) coexist within a single poisoned model, cannot be addressed by existing shortcut-based defenses that assume a single, static attack mechanism. Current multi-trigger remedies (BU+FT, BU+ANP, and BU+ABL) rely on backdoor unlearning, which incurs high training costs and loses effectiveness at low poisoning ratios. This paper proposes Combinatorial Lock, a training-free, reference-calibrated defense that reduces multi-trigger identification to a combinatorial problem over binary activation signatures. This formulation is the key novelty: it yields a multi-trigger defense that is training-free, trigger-oblivious, and directly implementable in hardware, since its decision rules can be evaluated with integer and logic operations. The framework combines anomaly-gated spectral scrubbing, which removes the malicious subspace only from inputs identified as anomalous, with a hash-compressed combinatorial signature verified by an ensemble of detection experts, including a compound-attack-aware expert for multi-trigger inputs. A joint threshold-shrinkage search identifies an operating point ($\tau$ at the 97.1st percentile, $\gamma = 0.78$) that reduces the attack success rate (ASR) to as low as 0.1% while preserving 97.8% clean accuracy. Evaluation on six models (ResNet18, VGG16, MobileNet, AlexNet, ViT-Small, ViT-Base) shows strong generalization: near-100% ASR drops to single digits across poisoning rates of 1-10% and 1-9 simultaneous triggers, with only gradual degradation in clean accuracy. ASIC and FPGA implementations confirm practicality, adding a consistent 19-20% latency overhead across all evaluated architectures and establishing Combinatorial Lock as a hardware-native approach to multi-trigger backdoor mitigation.

---


### 75. [From Intelligence to Autonomy: Foundations and Construction of Autonomous Agents for Future Intelligent Systems](https://arxiv.org/abs/2610.33445)

**<font color=#1a73e8>作者：</font>** Hongda Zhang, Ziqing Zhou, Yuning Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is moving from one-off perception and generation tasks toward long-term planning, tool use, and interaction with real environments. Greater task competence, however, does not automatically yield autonomy: an external actor may still have to set goals, sustain operating conditions, detect failures, and approve updates. We define an autonomous agent as a system that, within explicit identity and authority boundaries, maintains both task goals and viability conditions, acts continuously using models of the world and itself, and adjusts its control mechanisms and long-term capabilities through feedback. We trace the conceptual path from homeostasis and feedback control to autopoiesis and biological autonomy. We then distinguish six lines of operationalization: computational autopoiesis, behavior-based robotics, agent formalization, adaptive software, embodied adaptation, and robotic self-modeling. On this basis, we propose a one-boundary, four-loop framework in which Operational, Viability, Reflexive, and Learning loops organize task execution, self-maintenance, metacontrol, and governed learning. Five paired simulation experiments test permission constraints, road-closure response, health maintenance, capability re-estimation, and cross-task learning. Their results provide preliminary evidence for the feasibility of these mechanisms, while broader environments and physical systems remain to be tested.

---


### 76. [FG-ConvNO: A Geometry-Aware Neural Operator for Propeller CFD Prediction](https://arxiv.org/abs/2610.33456)

**<font color=#1a73e8>作者：</font>** Yichen Di, Valentin Duruisseaux, Di Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational Fluid Dynamics (CFD) is essential in contemporary engineering design, yet it remains expensive to compute and can take thousands of CPU/GPU hours or more for a single high-fidelity simulation. Recent developments in machine learning for scientific modeling have led to powerful surrogate frameworks that can approximate flow fields and physical quantities by using a fraction of the computational cost. However, most of these methods require largescale homogeneous datasets or simple geometries, exhibiting severe generalization gaps when applied to complex and data-scarce configurations. To address this, we propose the Factorized Geometry Convolutional Neural Operator (FG-ConvNO) for robust geometry-aware propeller pressure prediction under limited training data. We introduce geometryaware encoding, efficient interpolation-based decoding, and auxiliary global quantity supervision. In addition, we incorporate DISCO blocks that use discrete continuous convolutions to make the model discretization agnostic. In our experiments, FG-ConvNO achieves the highest accuracy for both surface pressure and global thrust prediction on a procedurally generated propeller CFD dataset. Geometry-aware encoding and architectural simplification improve stability, while random vertex subsampling enhances robustness. Overall, adding geometric priors to grid-based convolutional operators reduces overfitting on complex propeller geometries and improves generalization in low-data regimes.

---


### 77. [LegoSR: A Unified Framework for Self-improving Agent-Guided Scientific Discovery](https://arxiv.org/abs/2610.33465)

**<font color=#1a73e8>作者：</font>** Hao Mao, Xu T. Liu, Peng Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Equation discovery solvers often use different data interfaces, equation representations and evaluation criteria, making their results difficult to compare. We present LegoSR, a unified framework for algebraic symbolic regression and differential equation discovery. LegoSR integrates seven solvers through a common equation representation and evaluation process, and supports searches constrained by partially known equations. Researchers can run solvers directly or use LegoSR Agent, which selects solvers and adapts searches based on solver knowledge, intermediate results and lessons from earlier tasks. On noisy ordinary and partial differential equation benchmarks, LegoSR Agent recovers nearly as many equations as the union of seven expert-tuned solvers and outperforms a generic agent with the same model, tools and budget by up to 29 percentage points. Three examples demonstrate basic use, adaptive solver selection and discovery guided by partial physical knowledge.

---


### 78. [The Future Is Finer: Multivariate Time Series Super-Resolution Forecasting](https://arxiv.org/abs/2610.33470)

**<font color=#1a73e8>作者：</font>** Shuhao Li, Weidong Yang, Yue Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web platforms run on multivariate time series, from service telemetry and Web traffic logs to sensor streams served through Web APIs. Yet, retention policies often archive them at coarse granularity to save storage and bandwidth. Decisions such as autoscaling, alerting, and billing operate at finer granularity than existing forecasters reach, since these models predict at the resolution of their input. We therefore introduce Multivariate Time Series Super-Resolution Forecasting (MTS-SRF), which forecasts fine-grained futures from coarse histories, and propose TimeMagnifier to address its three challenges. Fourier Anchor counters data sparsity by fitting each input window to a trend-Fourier structure with sparse cross-variable gating; De-noise Only constrains fine-grained ambiguity by refining along the resolution axis rather than the noise axis, lengthening the grid level by level; and banded DTW Alignment corrects cross-resolution misalignment against the coarse forecast. On the first MTS-SRF benchmark, with ten datasets from five domains, real archived cross-resolution pairs, strengthened baseline adaptations, and five-seed significance tests, TimeMagnifier is best on every dataset, resolution coefficient, and metric against 15 baselines and cuts MSE by 12.3% on average. Its De-noise Only and DTW stages also transfer as a plug-in that lowers the MSE of existing forecasters by 5.1% to 9.0%. Code will be made publicly available.

---


### 79. [A Unified Analysis of Importance-Corrected Momentum Actor-Critic over a Markovian Trajectory](https://arxiv.org/abs/2610.33477)

**<font color=#1a73e8>作者：</font>** Yanjie Dong, Zhou Su, Wei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a generic actor-critic method that combines a ridge-regularized pathwise least-squares temporal-difference (LSTD) critic with importance-corrected momentum (ICM) actors. The critic solves a ridge-regularized system per frame by Newton-Schulz inversion and needs no stepsize, no knowledge of the mixing time, and no rank condition. Averaging stochastic policy gradients over frames of $T$ consecutive transitions, the ICM actors incur a frame-dependent gradient bias of order $\frac{1}{T}$. To our knowledge, we establish the first finite-time bounds for ICM actor-critic methods with normalized and unnormalized steps along a single Markovian trajectory. Up to a stationary-to-discounted distribution mismatch, the averaged gradient norm over $K$ updates is bounded by ${\cal O}(K^{-1/3}+\frac{1}{T})$ for normalized steps and by ${\cal O}(K^{-1/4}+\frac{1}{T})$ for unnormalized steps. We specialize these bounds to Muon, normalized stochastic gradient descent (SGD) with momentum, SGD with momentum, and AdaNorm, and compare them in the nuclear norm. With a dimension-free stepsize, Muon confines the factor $\min\{m,n\}^{1/2}$ associated with an $m\times n$ actor parameter matrix to the noise and correction terms. The comparison also characterizes when orthogonalization guarantees a larger noiseless ascent than normalization: exactly when the gradient's nuclear rank exceeds the spectral-to-Frobenius curvature ratio.

---


### 80. [Energy Efficient Lung Tumor Segmentation with a modified CBAM ENet Skip Model](https://arxiv.org/abs/2610.33479)

**<font color=#1a73e8>作者：</font>** Sharan Thummagunti, Aayushi Padia, Abhiram Koppuravuri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lung tumor segmentation plays a vital role in early detection and treatment planning of lung cancer. Although state-of-the-art deep learning models achieve high dice score coefficients (DSC), each forward pass requires computing large amounts of floating point operations, making them computationally expensive, requiring GPU acceleration, and having slow inference speed, limiting real-world clinical deployment. We propose a lightweight, energy-efficient model that leverages the ENet architecture for its real-time inference capability and low computational cost, enhanced with UNet-style skip connections between encoder and decoder stages for feature reuse and the lightweight Convolutional Block Attention Module (CBAM) for improved feature representation. The model is trained on publicly available data from The Cancer Imaging Archive (TCIA) via the Medical Segmentation Decathlon Challenge (MSD) and evaluated on the Lung Image Database Consortium and Image Database Resource Initiative (LIDC-IDRI) dataset. Our model achieves a DSC of 0.90812 (threshold of 0.5) with its compact architecture of 430,052 parameters and 0.549 Giga Multiply-Accumulate operations (GMAC), making it up to 10 times faster, requires 79 times less GMAC than UNet, and has 22 times fewer parameters than SegNet. These characteristics make it well-suited for deployment in clinical settings where computational resources are limited and decrease the cost of utilizing such a system. Additionally, the explainable AI technique of Grad-CAM is used to provide visual interpretability of the model's predictions and to identify regions where segmentation performance requires improvement.

---


### 81. [Climate downscaling with likelihood functional flow matching](https://arxiv.org/abs/2610.33482)

**<font color=#1a73e8>作者：</font>** Zhi-Song Liu, Helmi Toropainen, Michael Boy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decisions about heat, frost and flooding are made locally, yet reanalyses and climate models resolve tens of kilometres. Generative downscalers add kilometre-scale detail with uncertainty, but are tied to a grid, costly to sample and lack a tractable likelihood. Here we introduce CD-FFM, a functional flow-matching model that treats the high-resolution field as a continuous random field that one model can query at any location and resolution. Its velocity acts pointwise, so spatial variability comes from a noise prior fitted to the observed spectrum and every observation has an exact likelihood. Downscaling ERA5 to 1 km daily temperature over Fennoscandia, CD-FFM lowers the continuous ranked probability score by 27-31% against regression and 12-18% against a forty-times larger neural operator in each of three test years, and outperforms a CorrDiff-style diffusion model while sampling about fifty times faster. The same model transfers to precipitation and makes large kilometre-scale ensembles affordable.

---


### 82. [Error-Subspace Calibration for Multi-Task Model Merging](https://arxiv.org/abs/2610.33483)

**<font color=#1a73e8>作者：</font>** Yeseul Cho, Hanseul Cho, Chulhee Yun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging combines task-specific expert models into a single model without joint training on their original datasets, but often incurs a performance gap relative to the individual experts. Post-merging calibration can reduce this gap through task-specific representation alignment, but the alignment objective alone does not specify which feature directions to correct. We propose Error-Subspace Calibration (ESCal), a post-merging calibration framework that identifies low-dimensional error subspaces from weight differences between expert and merged models. At each intermediate block boundary, a bridge module projects the merged representation onto the next block's input-projection error subspace and maps these coordinates to an additive correction in the current block's output-projection error subspace. The subspace bases remain fixed, so calibration learns only these linear maps, yielding a parameter-efficient mechanism for feature correction. We find that ESCal brings the merged model closer to the experts in both representations and predictions, indicating more faithful recovery of task-specific behavior. Experiments on vision and natural language understanding benchmarks show that ESCal improves merged-model performance across diverse architectures and merging methods using a small calibration set for each task.

---


### 83. [Can One Hear Geometry? Gauge-Invariant Spectral Descriptors for Text-to-B-rep Retrieval](https://arxiv.org/abs/2610.33484)

**<font color=#1a73e8>作者：</font>** Hongzhu Yi, Hao Liu, Tao Yu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-3D solid retrieval requires aligning natural language with precise geometry despite variations in pose, scale, and recording conventions. Existing methods discretize Boundary Representation (B-rep) models into point clouds or meshes, or learn features from faces, edges, and topology, risking information loss or lacking explicit invariance guarantees. We propose a text-to-B-rep retrieval framework based on group actions and spectral geometric invariants, making invariance an explicit constraint on descriptor construction. Specifically, we use group actions to characterize equivalence transformations induced by translation, rotation, reflection, uniform scaling, and contour recording conventions. For sketch-extrusion solids, we construct a fixed 280-dimensional spectral geometric descriptor by integrating geometric information from three complementary levels, including cross-sectional regions, contour boundaries, and extrusion structures. Furthermore, we use descriptor-consistent multi-positive sets and geometric attribute supervision to promote structural alignment between text and solids. On Text-to-3D solid retrieval, our method achieves 88.6% Recall@5, exceeding the previous state of the art by 13.6 percentage points and demonstrating the effectiveness of explicit geometric invariants for precise 3D solid retrieval.

---


### 84. [Explicit Frictional Contact Modeling in Neural Garment Simulation](https://arxiv.org/abs/2610.33492)

**<font color=#1a73e8>作者：</font>** Thanh-Nguyen Truong, Vu-Hoang Tran, Ching-Chun Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) simulate garments efficiently through physics-based self-supervision, but leave body-garment friction implicit or inside training energies, with no friction coefficient $\mu$ to set at inference; retraining the tested GNNs with a coefficient-specific friction term barely responds to $\mu$. Optimization-based solvers decide each contact's stick-slip state from the reaction that governs it, but only by re-optimizing the garment state at every step; a friction term in a one-pass training objective acts as a fixed-weight penalty on sliding, and the trained weights apply no per-contact Coulomb condition at inference. We therefore resolve friction explicitly after prediction: a Modular Contact Operator, attached to a frozen predictor without retraining or an iterative solve, estimates the normal load, applies a closed-form Coulomb correction along a path across body triangles, and propagates the induced motion through the cloth as a linearized membrane wave. On HOOD and ContourCraft, it raises sticking and lowers slip monotonically in $\mu$, tracking a reference solver's response while coefficient-specific retraining stays flat, with low penetration and reference-consistent stretching at an eighth of the solver's runtime.

---


### 85. [RBGA: Residual-Budget Guide Arbitration for Offline-to-Online Safe Reinforcement Learning in Dexterous Manipulation](https://arxiv.org/abs/2610.33494)

**<font color=#1a73e8>作者：</font>** Zongyou Yu, Ao Zhou, Xiongbo Shi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dexterous manipulation requires robots to leverage existing datasets for rapid skill acquisition while maintaining safety during real-world deployment to prevent damage to the robot or its surroundings. Offline-to-online safe reinforcement learning (O2O safe RL) provides a promising solution for this problem by leveraging prior experience for online improvement under safety constraints, thereby mitigating the sample inefficiency and exploration risk of learning safe policies from scratch. However, existing O2O safe RL approaches do not explicitly account for the safety budget already consumed when making decisions within an episode. Excessive cost incurred early can therefore leave little room for subsequent exploration and policy improvement. To address this limitation, we propose \textbf{R}esidual-\textbf{B}udget \textbf{G}uide \textbf{A}rbitration (RBGA), an algorithm that explicitly tracks the remaining episode safety budget and uses it to adaptively select between offline guidance and the evolving online policy. At each step, RBGA compares the cost-to-go estimates of the guide and online actions against the remaining budget, enabling step-wise action arbitration throughout the episode. We provide theoretical analysis characterizing the safety implications of residual-budget-based selection and its effect on guide-assisted exploration. Extensive experiments demonstrate that RBGA enables effective online policy improvement while maintaining strong safety performance. Our code is available at this \href{this https URL}{link}.

---


### 86. [FreqPKC: Frequency-Aware PeakConv for Radar Semantic Segmentation](https://arxiv.org/abs/2610.33504)

**<font color=#1a73e8>作者：</font>** Yangyong Deng, Pengyu Zhang, Shaoqiu Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automotive millimeter-wave (mmWave) radar has attracted increasing attention for semantic segmentation in autonomous driving, owing to its robustness under adverse weather and lighting conditions. Recent works have introduced radar-specific neural operators such as PeakConv (PKC), inspired by constant false alarm rate (CFAR) detection, to better model the peak-dominated characteristics of radar images. However, existing methods typically treat the guard bandwidth as learnable parameters, without explicitly characterizing the frequency response of the PKC operator. In this work, we revisit PKC from a frequency-domain perspective and propose Frequency-Aware PeakConv (FreqPKC), which explicitly models and exploits its underlying spectral characteristics. By analyzing the frequency response of PKC, FreqPKC enables the network to capture a broader range of frequency components and adaptively adjust its effective bandwidth. With the proposed Frequency-Aware (FA) module, the network can infer appropriate guard bandwidths to balance high- and low-frequency information: it enhances high-frequency components in target regions for more precise segmentation while suppressing noise through low-frequency filtering in background areas. Building on FreqPKC, we further develop FreqPKC-Net, a radar semantic segmentation (RSS) framework that integrates frequency-guided adaptive modulation with cross-view fusion for multi-view inputs, and can also be adapted to single-view data. Experiments on the public datasets CARRADA, CARRADA-RAC, and a self-built dataset named RS-SAR demonstrate that FreqPKC-Net consistently outperforms existing SoTA methods on both range-Doppler and range-angle views.

---


### 87. [Eat Your Precision: Precision Objective Mitigates Reward Hacking in Rubric-based RL](https://arxiv.org/abs/2610.33512)

**<font color=#1a73e8>作者：</font>** Hyun Ryu, Jong-Heon Kim, Yiqing Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based rewards enable effective reinforcement learning on non-verifiable tasks. However, because these rewards are typically defined as a weighted measure of rubric coverage, models are trained primarily to maximize a recall objective. As a result, RL-trained models produce responses that are more complete but also more verbose and contain more unnecessary or factually incorrect content, leading them to be less preferred than responses from the base model. To address this issue, we present the FORK reward, which jointly optimizes recall and a novel precision objective, which requires each unit of a model response to be both necessary and factually correct, as measured by rubric-driven necessity credits and a factual-correctness grader, respectively. Our experimental results show that FORK outperforms existing rubric-based RL methods and achieves Pareto-optimal performance that balances rubric coverage and overall response quality. Compared to the original recall-based reward, FORK substantially improves precision and reduces response length while achieving similar rubric coverage, which leads to significantly higher win rate compared to the base policy (e.g., from 10.6% to 68.0% on RubricHub-Medical and from 22.1% to 74.1% on HealthBench).

---


### 88. [Overlap-Aware Sub-hypergraph Pattern Frequencies for Hypergraph-Level Classification](https://arxiv.org/abs/2610.33514)

**<font color=#1a73e8>作者：</font>** Nafiul Hasan Anik, Nazira Jesmin Lina, Md Tanvir Alam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classifying whole hypergraphs requires a fixed-length description of inputs whose numbers of vertices and hyperedges vary. Frequent sub-hypergraph patterns provide such a description, but previous work records only whether each pattern is present, which loses two kinds of information: how large the overlap between two hyperedges is, and how much of a hypergraph each pattern makes up. We extend frequent sub-hypergraph mining with overlap labels, the binned intersection size of two pattern hyperedges inherited from the target hypergraph, and represent each hypergraph by the relative frequency of each mined pattern. The vocabulary is mined from training hypergraphs only and then frozen, and validation and test hypergraphs are matched against it. A support rule that depends on pattern size keeps the vocabulary small. On the six hypergraph-classification datasets of DHG-Bench, with a single configuration chosen on validation scores, the method has a higher mean Macro-F1 than the best published mean on five datasets, by 18.67 points on Twitter-Friend and 10.02 points on Steam-Player; on RHG-3 it is 0.21 points lower. Ablations show that on Steam-Player and Twitter-Friend, replacing relative frequencies with presence lowers Macro-F1 by about 18 points, and that removing overlap labels lowers it by 4 to 9 points.

---


### 89. [Collective Collaboration of Recursive Autonomous Agents](https://arxiv.org/abs/2610.33515)

**<font color=#1a73e8>作者：</font>** Ziqing Zhou, Linqiang Hu, Yuning Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smart factories must translate order-level objectives into production tasks at multiple scales and combine the capabilities of individual units into an overall delivery capability. To address repeated adaptation of organizational mechanisms across equipment, workshops, and factories, as well as coordination across levels under changing production conditions, this paper develops a framework for the collective collaboration of recursive autonomous agents (RAAs). A common task and capability interface supports the recursive decomposition of production objectives from the top down and the aggregation of conditional capabilities through peer collaboration from the bottom up. Composite units can therefore participate in higher-level organizations as agents of the same kind. We formulate organizational models for leaf and composite units, specify interface closure under composition and conditions for finite task expansion, and develop operational mechanisms linking task decomposition, resource commitments, result aggregation, and coordination within the scope affected by change. A production network integrating machining, inspection, and logistics across multiple workshops illustrates how a common organizational kernel is instantiated at the equipment-service, workshop, and factory scales. The framework connects recursive organization with explicit task responsibilities, capability conditions, and execution interfaces for manufacturing systems.

---


### 90. [Component Pooling Trained Across Orientations for Few-Shot Remote Sensing Scene Classification](https://arxiv.org/abs/2610.33518)

**<font color=#1a73e8>作者：</font>** Bingchen Yan, Wenheng Guo, Yuye Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot remote sensing scene classification (FSRSSC) aims to recognize novel scene categories from only a few labeled images. Most FSRSSC methods summarize the feature map of an image by global average pooling, which treats the few objects that define an aerial scene and the large background around them alike, and they rarely consider that aerial images have no canonical orientation. To address these issues, we propose RoCoP, a parameter-free component pooling network trained across orientations. RoCoP consists of a feature extractor, a non-negative decomposition module (NDM) and a component scoring module (CSM). NDM factorizes the local descriptors of each image into a few additive components with a deterministic initialization and a single multiplicative update, so that the positions of one object are grouped together. CSM weights each component by its activation magnitude and converts the weights into a soft mask for pooling. Because both modules are invariant to permutations of feature positions, the only rotation-sensitive part of the pipeline is the backbone, which we train to classify randomly rotated views of every image. Experiments on NWPU-RESISC45, AID and UC Merced show that component pooling and rotated-view training are complementary: together they improve a strong transfer-learning baseline by about 2.5 points in 5-way 1-shot accuracy on NWPU-RESISC45 and AID, without adding parameters at inference. Under an identical protocol, RoCoP outperforms re-implemented metric-based and task-adaptive methods, and NDM and CSM also improve existing methods when plugged into them. We further identify the regime in which the method does not apply, namely very small base sets.

---


### 91. [Promise and Limits of Cross-Architecture Knowledge Distillation for Lightweight Medical Vision Transformers (LiteMed-ViT)](https://arxiv.org/abs/2610.33520)

**<font color=#1a73e8>作者：</font>** Shuaibu Shehu, Elijah M. Flomo, Mohammad Safiya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Running deep models for medical image analysis at the point of care is challenging with standard architectures: convolutional neural networks (CNNs) are often too heavy for edge devices, while Vision Transformers (ViTs) require massive training datasets to compensate for missing inductive biases. This study investigates how far the dual-token distillation used to train data-efficient ViTs can be pushed when applied across architectures, from a CNN-based teacher into a lightweight ViT student. LiteMed-ViT is introduced as a dual-token ViT featuring a convolutional stem and a class-balanced distillation objective; at 0.234M parameters, LiteMed-ViT carries 47.8x fewer parameters than its ResNet18 teacher at a memory footprint of just 0.89 MB. Evaluated against three compact CNN baselines on three MedMNIST subsets of varying modality and class balance, LiteMed-ViT attains higher accuracy than all three baselines on BloodMNIST (95.05%) and two on PathMNIST (89.15%). Under MedMNIST-C corruptions, it is at least as robust as every compact CNN across all subsets, outperforming them on BloodMNIST and PathMNIST without declining in relative standing as severity increases. Particular attention is devoted to identifying the exact conditions where performance plateaus. On DermaMNIST, LiteMed-ViT's balanced accuracy remains up to 1.9 points below the strongest compact CNNs and does not benefit from higher input resolutions up to 224 pixels, where ResNet18 gains 12.6 points. Stronger teachers do not yield a more accurate student, and overconfident ones lower its DermaMNIST balanced accuracy unless calibrated.

---


### 92. [Pacifo: An Efficient Fully Homomorphic Encryption-based Lightweight ResNet for Trustworthy Machine Learning as a Service](https://arxiv.org/abs/2610.33525)

**<font color=#1a73e8>作者：</font>** Yang Li, Gang He, Ruichen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine Learning as a Service (MLaaS) has become a popular paradigm for deploying AI applications. However, it raises significant privacy concerns that the raw client data needs to be uploaded to the server for inference services. Private inference using Fully Homomorphic Encryption (FHE) offers a solution by allowing computations directly on encrypted data, with only the final results decrypted on a client side. However, current practical implementations still suffer from large computational overhead and high latency due to the cost of FHE operations. In this paper, we propose Pacifo, a framework that adapts customized fine-tuning strategies to efficiently evaluate the ResNet20 model in the context of FHE. Specifically, Pacifo introduces a public-private layer partitioning scheme and an efficient ReLU approximation, significantly reducing the number of private layers and costly FHE operations during inference. It also offers flexible security configurations to accommodate varying client privacy requirements. Compared to state-of-the-art FHE implementations of ResNet20, Pacifo achieves a speedup of $3.7-21.7\times$ in runtime while effectively preserving $95\%-99\%$ of the original plaintext model accuracy across downstream tasks. Pacifo is open-sourced at this https URL.

---


### 93. [Security evaluation of 6G-oriented and O-RAN networks through targeted attacks](https://arxiv.org/abs/2610.33526)

**<font color=#1a73e8>作者：</font>** Apostolos Valiakos, Dimitrios Psaltis, Alexios Lekidis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The sixth generation (6G) of networks is supported by increased bandwidth, automation through the use of O-RAN technologies. Simultaneously though autonomous operation leads to an extensive threat surface and sophisticated attacks. Understanding the attack impact, the Tactics, Techniques and Procedures that are used by attackers is extremely challenging, but however is crucial for developing defense and mitigation strategies against them. This paper evaluates a targeted attack chain against a virtualized, 6G-oriented O-RAN testbed in which the F1 midhaul interface is accessible to an attacker and transport-layer protection is not enabled. The attack disrupts the legitimate O-DU association, introduces a rogue O-DU using observed configuration parameters, and intercepts user-plane traffic. The attack was evaluated in a fully virtualized testbed based on Open5GS, the srsRAN Project, FlexRIC, and an Electric Vehicle (EV) charging infrastructure based on OCPP 1.6.

---


### 94. [SkillShift-Bench: Benchmarking Skill Learning under Environment Evolution for Web Agents](https://arxiv.org/abs/2610.33528)

**<font color=#1a73e8>作者：</font>** Bo-Yu Chen, Zhi Zhou, Yu-Feng Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill learning enables web agents to reuse prior experience for long-horizon interactive tasks. However, learned skills are typically evaluated in closed environments, overlooking the fact that real-world web deployment involves continuous shifts in invocation context, perceptual grounding, and execution feasibility. To this end, we introduce SkillShift-Bench, the first benchmark for evaluating skill learning with controlled open-environment shifts. SkillShift-Bench simulates Contextual Shift, Perceptual Shift, and Execution Shift across three self-hosted web systems, and evaluates agents with diagnostics covering task success, interaction cost, skill use, and skill failure. Comprehensive experiments reveal systematic robustness degradation under controlled shifts, characterized by lower success rates, higher interaction costs, and more frequent skill failures, with Execution Shift exerting the strongest pressure. We further formulate shifted skill execution as a nonstationary local executability problem and provide both a dynamic-regret analysis and a practical test-time adaptation method, demonstrating the feasibility of improving learned-skill execution without relearning the skill library. Code, tasks, environments, documentation, and the leaderboard are available at this https URL.

---


### 95. [Clustering of High-Dimensional Human Gene Score Data for Target Cell Classification](https://arxiv.org/abs/2610.33531)

**<font color=#1a73e8>作者：</font>** S. Das, V. Madala, P. Majumder 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The goal is to investigate whether the total human gene-score dataset and the selected human kinase-gene dataset exhibit the same number of clusters when analysed using the same set of 769 features. Two datasets were considered: the complete gene score dataset and a subset containing selected kinase genes. Two missing-data strategies were investigated. In Case I, rows containing missing gene-score values were removed. In Case II, rows with more than 20% missing values were excluded and the other missing values were replaced by the corresponding column mean. For each case, the data were scaled and principal component analysis (PCA) was performed before clustering. Four clustering approaches were considered: K-Means, Hierarchical Clustering, Fuzzy C-Means, and Graph-based Clustering. Across both datasets and both missing-data treatments, the optimal number of clusters was found to be two. In the absence of an optimal number of clusters, the quality of clustering was assessed using the Silhouette score. Relatively high Silhouette scores were obtained in all cases.

---


### 96. [Patch-Derived or Register Tokens? Comparing Variable-Length Image Tokenizers](https://arxiv.org/abs/2610.33540)

**<font color=#1a73e8>作者：</font>** Philipp Schenkel, Tobias Schürmann, Omer Sahin Tas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image tokenizers convert pixels into compact latent sequences for efficient generative modeling. Most approaches arrange latents on a downsampled two-dimensional grid, tying sequence length to image resolution. We compare two variable-length strategies: computationally efficient patch-derived tokens, which inherit explicit spatial organization, and more demanding register tokens, which have no predefined spatial layout. Our reconstruction results reveal that patch-derived tokens perform substantially better under extreme compression, whereas register tokens achieve slightly better reconstruction quality at intermediate budgets. At high token budgets, both approaches achieve similar reconstruction quality. For downstream generative tasks, register tokens outperform patch-derived tokens. Adding representation alignment with external pretrained visual encoders substantially improves the generative performance of patch-derived tokens, allowing them to match or outperform register tokens depending on the token budget. We further find that both approaches learn spatially localized representations. Patch-derived tokens largely retain their explicitly imposed spatial organization, while register tokens develop an implicit two-dimensional spatial structure despite having no predefined layout. Representation alignment reduces this spatial organizational constraint, enabling individual tokens to exert a stronger non-local influence.

---


### 97. [Cross-Scale Sparse Attention for Referring Segmentation in Remote Sensing](https://arxiv.org/abs/2610.33551)

**<font color=#1a73e8>作者：</font>** Yuxi Li, Lu Si, Xia Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution remote sensing (RS) imagery provides fine spatial detail over large areas, making it essential for fine-grained scene understanding. Referring Remote Sensing Image Segmentation (RRSIS) aims to segment regions described by natural language, yet many existing methods rely on sequential alignment--fusion pipelines with limited joint modeling of cross-scale visual hierarchies and linguistic dependencies. Moreover, dense attention mechanisms struggle with the sparsity and wide spatial dispersion of RS targets, while current datasets offer limited structured evaluation of multi-target references, multi-hop relational reasoning, and multi-granularity descriptions, limiting both model development and evaluation. To address these challenges, we propose a Cross-Scale Sparse Attention Model (CSSAM), which aligns multiscale visual features with complex referring expressions through two key modules. The Cross-scale Modality-aligned Fusion Module (CMFM) performs unified cross-scale cross-modal fusion, while the Dynamic Multimodal Sparse Hybrid Attention (DMSHA) selectively attends to informative visual--textual tokens, reducing dense visual interactions. Furthermore, we introduce M$^{3}$RRSIS-D, a RRSIS dataset explicitly designed around three core reasoning dimensions: multi-target (M$^{1}$), reference-dependent multi-hop (M$^{2}$), and multi-granularity (M$^{3}$) expressions. Extensive experiments on M$^{3}$RRSIS-D and two public RRSIS benchmarks demonstrate that CSSAM achieves competitive performance across accuracy, fine-grained reasoning, and high-IoU localization metrics, validating its effectiveness for complex semantic reasoning in realistic RS scenarios. Code, dataset, and model weights will be released upon acceptance.

---


### 98. [End-to-end prostate lesion segmentation and detection from undersampled diffusion-weighted MRI](https://arxiv.org/abs/2610.33554)

**<font color=#1a73e8>作者：</font>** Lukas T. Rotkopf, Marco Schlimbach, Kevin Kröninger 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated prostate lesion detection from diffusion-weighted MR imaging (DWI) conventionally relies on reconstructed images and does not fully use all acquisition information. We present an end-to-end network that uses complex multicoil DWI data and coil sensitivity information for prostate lesion segmentation.
We included 269 fastMRI prostate examinations with additional voxel-level lesion annotations. Of these, 64 examinations contained PIRADS 4 or 5 lesions. The proposed network, VarNet-Seg, consists of a k-space variational network (VarNet) with six variational cascades and an image-space 3D segmentation U-Net. Comparator models used the same segmentation architecture with fully coil-combined images (CC-Seg), fixed root-sum-of-squares reconstruction (RSS-Seg), or fixed SENSE reconstruction (SENSE-Seg). We performed ablations with end-to-end training and data consistency (DC) enabled or disabled. We evaluated lesion segmentation using Dice and patient-level detection using AUROC in five-fold cross-validation with full sampling, simulated undersampling, added noise, or both.
VarNet-Seg achieved the highest Dice at every undersampling level. At eight-fold acceleration, Dice was 0.22 for VarNet-Seg, 0.14 for SENSE-Seg and 0.16 for VarNet-Seg (no DC). The paired difference from SENSE-Seg was 0.08 (95% CI, 0.04-0.11). With full sampling, VarNet-Seg and RSS-Seg performed similarly (0.40 vs 0.39). Patient-level AUROC decreased from 0.75 with full sampling to 0.63 at eight-fold acceleration; corresponding RSS-Seg AUROCs were 0.76 and 0.64.
The proposed multicoil network improved prostate lesion segmentation under simulated undersampling compared to conventional models. Matched ablations supported contributions from both end-to-end training and data consistency. Prospective evaluation is needed to establish whether this approach can be used clinically in accelerated prostate DWI.

---


### 99. [Nowcasting aerosol particle size distributions from PM2.5 with physics-regularized flow matching](https://arxiv.org/abs/2610.33557)

**<font color=#1a73e8>作者：</font>** Zhi-Song Liu, Jenni Köykkä, Wenqing Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The mass concentration of particles smaller than 2.5um (PM2.5) is cheap to measure and widely monitored, whereas the particle number size distribution (PSD) requires costly instruments and is measured at only a few research stations. Yet many aerosol effects, such as vapor uptake, cloud droplet formation and deposition in the human respiratory tract, depend on the PSD rather than on mass. We explore whether recent generative deep learning models can nowcast the PSD: from the PM2.5 record and eight meteorological parameters over a 24h window, a model generates an ensemble of plausible hourly size distributions for the same window, reflecting that one mass can arise from many size distributions. Rather than proposing a single best model, we use two contrasting Finnish stations, the boreal forest site Hyytiälä and the urban site Kumpula, as a controlled testbed. On it, we benchmark six generative models against deterministic and climatological baselines, locally and after transfer between sites, and test physical constraints for neural network training. Flow matching performs best overall; its guided variant has the lowest continuous ranked probability score (CRPS) at both sites. A constraint based on a reduced aerosol general dynamic equation (GDE) lowers the CRPS by 5.5-11.5% at the training site and reduces errors after transfer between sites. Transfer remains harder than local estimation, identifying training on large multi-station data sets as the next step towards PSD estimates at unmonitored locations. This benchmark establishes physics-informed generative models as a promising route from routine air-quality monitoring to size-resolved aerosol information.

---


### 100. [Distilling Dense Trajectory Teachers For Large-Motion Video World Models](https://arxiv.org/abs/2610.33566)

**<font color=#1a73e8>作者：</font>** Shuofeng Sun, Linqing Zhao, Haibin Yan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models are expected to generate videos that accurately follow specified camera trajectories while maintaining consistent 3D structures. However, existing models are predominantly trained on densely sampled videos with small inter-frame camera motions. When applied to sparse, large step trajectories, they often produce frozen frames, inaccurate camera motion, and severe geometric drift. We attribute this degradation to a mismatch between the gradual viewpoint transitions seen during training and the large viewpoint changes required at inference time. To address this problem, we propose Dense Trajectory Teacher Distillation (DTTD), a post-training framework that transfers a model's generation capability from dense trajectories to large camera motions. Given a sparse trajectory, DTTD interpolates additional camera poses to construct a dense trajectory covering the same path. The frozen base model then generates reliable teacher videos along this familiar dense trajectory, and pose aligned teacher observations are used to evaluate candidate videos generated under the original sparse trajectory. In this way, the model serves as its own generation teacher, requiring neither additional video data nor a stronger external video generator. We further combine dense teacher supervision with geometry aware rewards that assess cross frame consistency and camera trajectory following, and use the resulting preferences for offline preference optimization. To stably expand the model's motion range, we introduce a cumulative curriculum that progressively incorporates larger motion steps while retaining simpler trajectories to reduce capability forgetting.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-446](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
