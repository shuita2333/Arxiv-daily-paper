# 📦 其他研究 | 2026年10月09日

> 本类共 **324** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-324](./part-07.md)

---

### 251. [Argos: Adapt Rich Geometric Priors for Generalizable Online Scene-Change-Detection](https://arxiv.org/abs/2610.10181)

**<font color=#1a73e8>作者：</font>** Ruihan Xu, Jiae Yoon, Kaichen Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robots operating in dynamic environments require reliable detection of how their surroundings change over time. Existing learning-based methods largely rely on pairwise 2D image features, which struggle under large viewpoint changes and occlusions, are sensitive to noise, and show limited generalization across domains, while explicit 3D approaches typically require costly offline optimization. We show that the implicit 3D knowledge of Geometric Foundation Models (GFMs) provides a strong basis for addressing these limitations. We introduce Argos, which adapts GFM features for joint scene change detection and 3D reconstruction. To address data scarcity and take a step toward a foundation model for scene change detection, we introduce a large-scale benchmark comprising two synthetic datasets and one real-world dataset, and train jointly across diverse datasets to improve cross-domain generalization. We further introduce Argos-SLAM, a real-time system designed for robotics, which performs online change detection and change-aware 4D mapping. Across benchmarks, our framework substantially outperforms existing baselines, with gains of up to 42.01% in change IoU and 27.91% in F1, while supporting scalable deployment in changing real-world environments.

---


### 252. [EEG and Eye-Tracking Evidence That AI Disclosure Shapes Face Evaluation](https://arxiv.org/abs/2610.10182)

**<font color=#1a73e8>作者：</font>** Teodora Mitrevska, Luise Donat, Andreas Butz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-generated faces can be difficult to distinguish from real ones, leaving viewers to rely on source labels when judging an image. Yet prior work has made it difficult to separate the effects of what an image actually is from what viewers are told it is. We validated faces as AI-generated or human in an online study (N=169), then crossed actual source (AI, human) with label (none, Made with AI, Made by a human) in a lab study $N=30), recording event-related potentials (ERPs) and gaze. ERP responses were equivalent for AI-generated and real faces, but varied with the label: labels drew early attention (N2), while labels that conflicted with the face's actual source prompted re-evaluation of the face (P3). Affective processing and initial gaze orienting were unchanged, but labels altered visual exploration. We provide a validated stimulus set and evidence that attributed origin shapes face processing, with implications for disclosure design.

---


### 253. [Pre-training of Bayesian Optimization Algorithm through Bayesian Optimization](https://arxiv.org/abs/2610.10186)

**<font color=#1a73e8>作者：</font>** Satoshi Katayama, Shoyo Hunt, Shintaro Masuda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) is widely used as a standard approach for expensive black-box optimization. However, BO algorithms often involve parameters that must be specified in advance, and their performance can strongly depend on these choices. We propose a framework for optimizing such parameters using sample paths drawn from a Gaussian process (GP) inferred from the information available at the start of BO. We use cumulative regret as the performance metric for a BO algorithm. By running the BO algorithm on the generated sample paths, we obtain an empirical estimate of its expected cumulative regret for a given parameter configuration. Optimizing this estimate allows us to identify parameter configurations that, given the currently available information, are expected to achieve low cumulative regret. Since this parameter optimization is itself a black-box optimization problem, we employ another BO procedure to solve it, which we refer to as outer BO. Through experiments, we demonstrate that the proposed framework can effectively select parameter configurations that achieve strong performance among a range of candidate configurations.

---


### 254. [HuLiGen: Human LiDAR Generation from Parametric Body Models](https://arxiv.org/abs/2610.10196)

**<font color=#1a73e8>作者：</font>** Salma Galaaoui, Nermin Samet, David Picard  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR point clouds of humans are extremely expensive to collect and annotate, thus represent a scarce resource that hinders the development of human analysis using this modality. To alleviate this scarcity, prior work relies on simulated human LiDAR, but such samples do not fully reflect the geometry and sensing characteristics of real observations. In contrast, we introduce HuLiGen, a generative model that generates human LiDAR point clouds from a parametric body model, using a point transformer trained with a flow-matching objective. We show that our generated point clouds are closer to the real capture distribution. Using HuLiGen to generate synthetic data, we propose a synthetic-only pretraining scheme for LiDAR-based HPE that achieves state-of-the-art performance, with even larger gains in low-annotation and low-data regimes, where MPJPE is reduced by up to 50%. Code, models and generated samples are available at this https URL.

---


### 255. [VolCo: Volumetric Contact for High-Fidelity Human Grasp Generation](https://arxiv.org/abs/2610.10197)

**<font color=#1a73e8>作者：</font>** Zhuo Chen, Yihua Cheng, Aleš Leonardis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate contact modeling is fundamental to understanding hand-object interaction, yet existing contact representations are typically restricted to object surfaces and rely on hand-crafted rules to recover contact details, leading to severe penetrations and implausible results. To better exploit the rich detail in motion-capture data, we introduce Volumetric Contact (VolCo), a representation that expands surface points to a set of 3D volumetric grids. VolCo encodes 3D contact that allows precise hand part recovery, and is organized in an inherent hierarchy: local contact details within each volume and global hand geometry across all volumes. Our framework, VolCoDiff, employs two modules to capture local and global features following this hierarchy. For local contact details, we use a 3D variational autoencoder to model the possible hand configurations conditioned on the local object signed distance field (SDF). For global hand geometry, we design a prior-guided diffusion model that learns the distribution of compressed latent features aggregated from the volumetric grids. We evaluate our method on two benchmark datasets and demonstrate state-of-the-art performance in penetration and stability, indicating the capability to generate tight grasps with much less severe penetrations. Our code is available at this https URL.

---


### 256. [How to train your model organism](https://arxiv.org/abs/2610.10203)

**<font color=#1a73e8>作者：</font>** Xilin Wang, David Bau, Byron C. Wallace  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model organisms of alignment-relevant behaviors (e.g., backdoors, sycophancy, spurious correlations) have emerged as a key tool for evaluating whitebox interpretability techniques. We argue that the prevailing practice of training model organisms to a single objective of installing the target behavior is insufficient and propose validating model organisms with respect to three objectives with associated metrics: target-behavior installation, general-capability preservation (i.e., parametric knowledge, chat quality), and output naturalness (i.e., CoT and activations). We re-visit two publicly released organism suites using this validation framework and show that (1) chat quality and CoT naturalness degrade substantially across training recipes, and (2) validation metrics predict how well interpretability methods recover the installed behavior, e.g., a logit lens readout covaries with an organism's general capabilities. We introduce a multi-objective training approach based on model merging to train more realistic model organisms. Finally, on a new suite of model organisms targeting demographic biases in clinical reasoning, we compare training recipes and find that DPO training stays closer to the base model than supervised finetuning, and the proposed model optimization approach better preserves capabilities and naturalness. Auditing this suite with an investigator agent, we again observe validation metrics tracking bias recovery. In sum, training methods shape the interpretability conclusions an organism supports, and we argue that one should consider multiple objectives to draw generalizable conclusions about interpretability methods using (realistic) model organisms.

---


### 257. [OrthoGen: A Generative Orthogonal Learner for Time-Varying Treatments](https://arxiv.org/abs/2610.10210)

**<font color=#1a73e8>作者：</font>** Tomàs Garriga, Valentyn Melnychuk, Konstantin Hess 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating conditional distributional potential outcomes (CDPOs) over time is important in medicine (e.g., to estimate patient-specific risks under different treatment sequences). However, this task is challenging because of time-varying confounding, yet existing adjustment strategies for this task are limited. In this paper, we aim to learn CDPOs under time-varying treatments using flexible generative models. Our contributions are two-fold. (1) We introduce a tailored adjustment strategy for our setting, namely, generative recursive g-computation. Our adjustment strategy recursively propagates full conditional outcome distributions rather than conditional means, modeling the variables of interest directly rather than full trajectories. Building on our adjustment strategy, we formulate simple generative learners for CDPO estimation. However, these learners can be sensitive to nuisance estimation errors, which motivates an orthogonal learner. (2) We thus introduce OrthoGen, a Neyman-orthogonal and doubly robust generative learner. Importantly, we show that OrthoGen further achieves rate double robustness and quasi-oracle efficiency under suitable conditions. Our learners are flexible and can be instantiated with different generative backbones (e.g., normalizing flows and diffusion models). Across experiments with synthetic, semi-synthetic and real-world datasets, we find that OrthoGen is highly effective. To the best of our knowledge, we are the first to propose a generative orthogonal learner for estimating CDPOs under time-varying treatments.

---


### 258. [Edge Accuracy Is Not Enough: Why Dynamics-Learned Structure Fails to Transfer to Inverse Problems](https://arxiv.org/abs/2610.10213)

**<font color=#1a73e8>作者：</font>** Nicholas Tan Jerome, Fangnian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A natural strategy for inverse problems with scarce labelled data is to transfer relational structure learned from abundant forward-simulation data. We show this strategy fails systematically, even when it satisfies the standard theoretical justification for why structure should help. We prove that approximate structure provides estimation-error benefits whenever the edge error satisfies $\Delta < n^2 - kn$, reducing sample complexity from $O(n^2)$ to $O(kn+\Delta)$. Structure learned via Neural Relational Inference (NRI) from dynamics prediction satisfies this condition, yet on a source-localisation task across 180 CFD-simulated hydrogen-leak scenarios and 180 acoustic scenarios, it degrades performance by 116% and 201% relative to a flexible, task-optimised attention baseline, while a physics-based prior (Green's function) degrades by only 69-72%. Four independent lines of evidence show this is not a tuning failure: NRI improves only 0.5% when given 18x more training data (versus 16.6% for the task-optimised baseline, $p<0.001$); performance is insensitive to the NRI edge threshold across a wide range; the dynamics-learned graph overlaps the task-optimal graph on only 6% of edges; and two further dynamics-derived structure estimators (correlation- and mutual-information-based) show no measurable benefit over a structure-free baseline, with the correlation-based estimator performing markedly worse. We formalise this gap as a statement about approximation error that the edge-accuracy condition cannot control, and we provide a lightweight transferability test (Jaccard similarity against a partially-observed target-task graph) that separates successful from failed transfer in all four domain/structure pairs we evaluate, using under an hour of computation and 15-20% of target-domain data; we present this as a heuristic calibrated on few cases, not a validated general threshold.

---


### 259. [Finite-Sample Approximation of Hessian-Guided Perturbed Wasserstein Gradient Flows](https://arxiv.org/abs/2610.10218)

**<font color=#1a73e8>作者：</font>** Ryotaro Kawata, Atsushi Nitanda, Taiji Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wasserstein gradient flow extends gradient descent to probability measures. Its Hessian-guided perturbed variant (PWGF) adds Gaussian perturbations to escape saddle points in nonconvex problems. We investigate when its approximation by finitely many interacting particles remains accurate over growing time horizons. Our analysis retains the curvature accumulated along the population-driven reference path: negative curvature can amplify approximation errors, while subsequent positive curvature can damp their influence. This captures favorable scenarios in which temporary instability is compatible with accurate tracking over growing horizons. Under regularity assumptions and a prescribed common perturbation schedule, we prove particle and objective-value tracking bounds on a high-probability event for reference paths satisfying explicit conditions on accumulated curvature. To handle state-dependent Gaussian jumps, we construct a population-first coupling that preserves the reference particles' conditional independence and reduces jump errors to covariance comparison. We verify the conditions in a variance-plus-cosine model, where curvature recovery yields a growing-horizon tracking guarantee. We also establish local attraction, transverse descent, and positive second variation in two regions of a regularized matrix-factorization model, motivating a positive-negative-positive curvature pattern.

---


### 260. [Evaluating Sequence Assembly Strategies for Differentially Private Synthetic Time-Series Forecasting](https://arxiv.org/abs/2610.10222)

**<font color=#1a73e8>作者：</font>** Guoxiong Long, Huizhen Huang, Qikun Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private time-series generators commonly produce fixed-length synthetic windows, whereas downstream forecasting models often require long continuous training sequences. How these windows are assembled after generation can therefore alter the effective synthetic data presented to a forecaster, even when the trained generator remains unchanged. We study this post-generation sequence assembly process by systematically varying overlap rates and window-weighting schemes and evaluating the resulting sequences in terms of boundary continuity, statistical and temporal fidelity, and Train-on-Synthetic-Test-on-Real (TSTR) forecasting utility. Across four types of public datasets (ETTh1, ETTm1, Weather, and Appliances) and five forecasting models, the results reveal a clear forecaster-dependent assembly principle: downstream TSTR utility is jointly shaped by the forecaster, overlap rate, and window-weighting scheme, leading to distinct assembly preferences across forecasting models. Increased overlap generally improves boundary continuity, but improvements in continuity or individual fidelity diagnostics do not consistently reduce forecasting error, indicating that these diagnostics alone are insufficient for selecting assembly configurations. Complete five-forecaster assembly grids, together with matched Train-on-Real-Test-on-Real (TRTR) references, further characterize these regularities and quantify assembly-dependent utility relative to real-data training. We then validate the identified principles through additional analyses of robustness and generator variability.

---


### 261. [Masked Feature Encoding for Large-Scale Whole Slide Image Representation](https://arxiv.org/abs/2610.10225)

**<font color=#1a73e8>作者：</font>** Haoyu He, Basile Tessier-Cloutier, Yang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole slide image (WSI) analysis in computational pathology follows a multiple instance learning (MIL) pipeline where patch embeddings are extracted independently and aggregated for slide-level prediction, but within-slide variance from staining, scanner, and local texture can overwhelm the discriminative signal. We propose Masked Feature Encoding for Multiple Instance Learning (MFE-MIL), a feature-space masking framework that trains a lightweight MLP adapter jointly with a window-based masked reconstruction branch and a MIL classification head. The two objectives are complementary. Classification guides the adapter to suppress within-slide patch variance, while window-based masked reconstruction provides an auxiliary regularizer for the adapted features without using patch coordinates, coordinate graphs, or segmentation preprocessing. The raster patch-extraction order is used only as a weak implicit prior. At inference, the decoder is removed, leaving only the adapter and MIL head. Across CAMELYON16/17, PANDA, and TCGA-BRCA with four diverse encoders, MFE-MIL improves ACC/F1 for nearly all tested aggregator-encoder settings and AUC in most, outperforms coordinate-based spatial methods (CAMIL), and achieves higher AUC than 2DMamba on three of four datasets (UNI). On five TCGA survival cohorts it improves the average concordance index for every aggregator tested, its most consistent gain. Code is available at this https URL.

---


### 262. [ProtocolMatch: Protocol-Dependent Model Selection for Scientific Dynamics Forecasting](https://arxiv.org/abs/2610.10239)

**<font color=#1a73e8>作者：</font>** Lu Wei, Yufeng Wang, Haibin Ling  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific dynamics forecasting is often framed as an architecture choice, although deployment is also determined by observed history, rollout feedback, compute budget, physical objective, and test distribution. We formulate protocol-dependent model selection and introduce ProtocolMatch, a compute-matched, validation-selected, and failure-preserving evaluation framework. On driven quantum-spin dynamics, we compare recurrent, patched-attention, causal-attention, and low-rank linear predictors across three independently generated datasets. The causal-attention--recurrence ordering reverses as the training set grows within a fixed two-spin task, while a linear predictor has the lowest mean error in the six-spin local-observable comparison. Restricting observed history worsens every refreshed-history view but improves every closed-loop view in the four-spin study. A latest-state MLP has lower error than persistence on every dataset under state refresh across all five cells, yet its closed-loop rank varies by system and includes finite explosive errors. Physical penalties improve targeted consistency without reliably improving prediction error, and in-distribution intervals lose most coverage after a driving-frequency shift. Thus scientific model selection should return a predictor with its protocol and report accuracy, physical validity, and shifted-distribution reliability separately.

---


### 263. [MorphCL: Morphological Contrastive Learning for Inertial-based Human Activity Recognition](https://arxiv.org/abs/2610.10245)

**<font color=#1a73e8>作者：</font>** Marius Bock, Yuwei Zhang, Juergen Gall 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the ubiquity of sensors in wearable and mobile devices and the abundance of human movement data they generate, translating unlabeled recordings into foundational motion models remains an open challenge. Self-supervised learning (SSL) has alleviated the need for costly annotations, yet existing approaches leave the global structure of large-scale motion data largely untapped, relying on randomly sampled batches and local comparisons that become particularly problematic for in-the-wild inertial data dominated by stationary, low-variance behaviors. Here we introduce Morphological Contrastive Learning (MorphCL), a self-supervised pretraining framework that uses structure-aware grouping to inject explicit modeling of global structure into inertial-based SSL approaches. Building on two well-established pillars of motion analysis, the discovery of motion primitives, or motifs, and domain-specific feature descriptors, we show that MorphCL substantially improves linear probing and finetuning results of learned encoders by up to 15 percentage points in F1-score. In a comparison with existing foundation models, we demonstrate that MorphCL-pretrained encoders match or surpass them models in linear probing performance while trained on $4600\times$ less data. Qualitative analysis of the resulting embedding spaces further reveals morphologically meaningful cluster structure, with improved separation of kinematically similar activity classes.

---


### 264. [Stationary Bias and Extrapolation in Nonlinear Two-Timescale Stochastic Approximation](https://arxiv.org/abs/2610.10246)

**<font color=#1a73e8>作者：</font>** A.Ch. Madhusudanarao, Rahul Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constant-step stochastic approximation generally has a nonzero stationary mean error that persists under time averaging. This paper studies that error for nonlinear two-timescale recursions driven by an exogenous finite-state Markov chain. Under stated smoothness assumptions and conditions on the stationary distribution, we derive a first-order bias expansion whose error bound remains uniform as the slow step size becomes much smaller than the fast step size. Fast-manifold coordinates keep the associated covariance equation regular in this limit. For fast step $\eta$ and slow step $\varepsilon$, the expansion reveals a mixed contribution $\varepsilon^2/\eta$ alongside terms linear in each step size. This dependence matters for bias reduction: along power-law step-size paths, the bias exponents need not be integers, so Richardson--Romberg extrapolation requires weights matched to the path. An exactly solvable nonlinear Markov example verifies the coefficients. We verify localization for temporal-difference learning and compare finite-run extrapolation at equal update budgets. For finite runs, we bound the initialization error of tail averages on both timescales under an additional coupling assumption. In the special case of additive independent noise, signed third-moment cancellation yields a sharper remainder.

---


### 265. [Logarithmic Regret via Passive Change Detection in Piecewise-Stationary Self-Tuning Regulation](https://arxiv.org/abs/2610.10250)

**<font color=#1a73e8>作者：</font>** A.Ch. Madhusudanarao, Rahul Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study minimum-variance control of an unknown autoregressive system with exogenous inputs and coefficients that change at unknown times. Under bounded independent disturbances, fixed detection gaps, stability and feasibility conditions, and sufficient time between changes, we prove \(O((C+1)\log((T+1)/\delta))\) regret with probability at least \(1-\delta\), where \(T\) is the horizon and \(C\) the number of changes. Unlike switching bandits, where unselected arms can change unobserved, admissible plant changes provide information during exploitation: the correct feasible controller leaves only the disturbance in the output, whereas a detectable change raises output energy under the old controller. PIECE-CD explores initially and after alarms, then uses gated recursive least squares for control. Its energy test compares windowed output power with a threshold above the noise floor; the extension to unstable controller mismatches also monitors the reference controller's input proposal. We control false alarms across the horizon and prove logarithmic detection delay. Inputs are clipped to prescribed bounds. Logarithmic regret also holds under an explicit condition ensuring that clipping becomes inactive after a finite burn-in. Under the stated feasibility conditions, the extended detector covers destabilizing changes with detectable excess energy over a fixed window.

---


### 266. [OOM-RL II: Reality Is an Oracle, Not a Debugger Provenance-Constrained Diagnosis in Continually Evolving Agent-Engineered Systems](https://arxiv.org/abs/2610.10256)

**<font color=#1a73e8>作者：</font>** Kun Liu, Liqun Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reality may establish that an outcome occurred without identifying which evolving procedure produced it or why. This distinction matters in production ML systems whose code, configuration, and artifacts change while external feedback accumulates. We examine it in a human-directed, agent-engineered quantitative trading system, using oracle to mean an external source of realized outcomes rather than a complete correctness specification. Across one year, the account gained and outperformed a broad market index, while annual alpha was not statistically distinguishable from zero under the main retrospective specification. Retrospectively selected subperiods include adverse relative performance and conditional candidate-level weakness under declared approximate references. Engineering records document changes during the episode, and complete recommendation-to-runtime binding is unavailable. The archive does not establish a common frozen instance or a unique cause. The case motivates an outcome--diagnosis gap: outcome evidence, evaluated-object identity, and causal explanation support distinct claims. We distinguish frozen instances, pre-specified adaptive procedures, and ad-hoc development; organize archive-relative claim identifiability and an evidence hierarchy; and propose a prospective production-binding protocol. An illustrative compatible-history example shows how factual binding can resolve a recommendation's referent without supplying its counterfactual effect. The protocol is proposed rather than prospectively validated. External feedback constrains outcome claims, while provenance and additional identification structure determine the resolution of diagnosis.

---


### 267. [PairAudit: Guiding Human Review with Graph Tokens under Distribution Shift](https://arxiv.org/abs/2610.10260)

**<font color=#1a73e8>作者：</font>** Jiran Tao, Binyan Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intrusion detectors can confidently misclassify attacks that were not seen during training. Human review can correct these errors, but only a limited number of cases can be checked. Uncertainty-based review may overlook confident errors, while anomaly scores alone do not show whether changing the review plan will correct more errors. We introduce PairAudit to find overlooked errors and improve review under a fixed budget. Its graph tokens capture prediction patterns across connected nodes. Rather than building another predictor through feature aggregation, PairAudit uses unusual relational patterns to uncover potential errors in existing predictions. Human feedback then helps decide whether these findings justify changing review priorities. Experiments across security tasks show that PairAudit corrects more errors on average than uncertainty-based review, including more errors on unseen attacks. These gains account for all review costs and do not require retraining the detector.

---


### 268. [LoomSC: Scalable Deep Subspace Clustering with Projector Factorization and Exact Spectral Reduction](https://arxiv.org/abs/2610.10266)

**<font color=#1a73e8>作者：</font>** Nairouz Mrabah, Youssef Melki, Mohamed Bouguessa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense self-expression matrices and full-affinity spectral clustering limit the scalability of subspace clustering. We introduce the Latent Orthogonal Optimization Model for Subspace Clustering (LoomSC), a framework that addresses both bottlenecks through projector factorization and exact spectral reduction. Motivated by the spectral structure of least-squares regression, LoomSC jointly learns latent features and a projector self-representation through two thin factors. Alternating Procrustes and least-squares updates preserve the sample factor's orthogonality while keeping the coefficient matrix implicit. We construct a nonnegative quadratic affinity that preserves the projector's support. An exact feature map then reduces its normalized spectral problem to an eigenproblem whose dimension depends only on the factor width. Neither the full affinity nor the sample Laplacian needs to be formed. Our analysis quantifies the projector approximation and identifies conditions for subspace preservation and within-subspace connectivity. For fixed dimensions and iteration budgets, the complete pipeline has linear time and memory complexity in the number of samples. Across five image-clustering benchmarks, LoomSC ranks first or second in all 15 dataset-metric comparisons against 9 state-of-the-art baselines. Its mean accuracy exceeds the highest baseline mean by 6.66 percentage points. Synthetic experiments scale to 500,000 samples while maintaining at least 99.8% accuracy.

---


### 269. [Video Prediction Policy 2: Predict Better, Act Better](https://arxiv.org/abs/2610.10270)

**<font color=#1a73e8>作者：</font>** Yanjiang Guo, Haodong Yan, Zhide Zhong 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) have emerged as an important class of generalist robot policies, aiming to transfer video prediction priors to action learning. However, we find that existing WAMs frequently produce incorrect motion predictions in open-ended environment, leading to erroneous actions. We attribute this limitation to two factors: (1) base video models are not optimized for manipulation, and (2) naively incorporating action components into video models can substantially degrade their generalization capabilities. We introduce Video Prediction Policy 2 (VPP2), a WAM that enables strong zero-shot generalization in both video prediction and action generation. First, we curate a large-scale, diverse dataset of manipulation videos to continue pretraining the base video foundation model. We annotate video clips with detailed captions and perform \textit{event-level} video pretraining to promote generalization across open-ended manipulation tasks. Second, we post-train and distill the video model into a single-step visual planner with fixed prediction horizon. Finally, we introduce action module via a mixture-of-transformers (MoT) architecture to learn implicit inverse dynamics model. Experiments demonstrate three key results: (1) VPP2-14B outperforms Cosmos3-64B by 11.0\% points in video prediction instruction-following success rate on open-ended tasks; (2) VPP2 surpasses the strongest baseline by 18.5\% points in success rate on real-world zero-shot ALOHA manipulation tasks; and (3) following benchmark-specific post-training, VPP2 achieves the highest success rates among evaluated methods on the challenging LIBERO-Pro, LIBERO-OOD, and RoboDojo benchmarks.

---


### 270. [A Closed-Loop Non-Asymptotic Convergence Analysis of PPO with Learned Critics and Clipping](https://arxiv.org/abs/2610.10273)

**<font color=#1a73e8>作者：</font>** Junwei Su, Mengfan Liu, Yanyong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite its widespread use, Proximal Policy Optimization with clipping (PPO-Clip) remains difficult to tune, and the interactions among critic learning, clipping, and rollout reuse remain incompletely understood. We develop a \emph{non-asymptotic} analysis of PPO-Clip as a \emph{closed-loop actor--critic} system. It captures actor--critic coupling, nonsmooth probability-ratio clipping, finite-batch reuse, and predictable early stopping under explicit coverage and critic regularity assumptions, using raw GAE and Monte Carlo critic targets. Our synchronous and asynchronous guarantees jointly characterize policy stationarity and the tracking accuracy of the learned critic, with explicit dependence on algorithmic parameters. A sufficient coupling condition gives optimization, critic tracking, clipping, and finite-batch errors a common amplification bound. The asynchronous result also requires a delay-dependent critic stepsize restriction; violating these conditions does not establish divergence. For finite layered MDPs with tabular critics, a uniform bound on the actual clipped-gradient class replaces complete-trajectory counting. A verified growing-horizon family has polynomial sample complexity, and a two-time-scale schedule gives $O(T^{-2/5})$ stationarity and critic-tracking bounds with explicit fresh-rollout accounting. These results together advance our understanding about PPO and provide theoretical guidance in tuning.

---


### 271. [Sparse Planning in Visual World Models via Cost Gradients](https://arxiv.org/abs/2610.10274)

**<font color=#1a73e8>作者：</font>** Yingchen Xu, Edward Grefenstette  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Token-based world models enable fine-grained latent planning, but repeatedly processing large spatial token grids makes action search expensive. We introduce COSTGRAD, a training-free, goal-conditioned selector that ranks spatial tokens by the gradient norm of the planning cost with respect to each input token. By deriving importance from the downstream control objective, COSTGRAD targets tokens that matter for planning rather than merely for prediction. On AdaLN-conditioned predictors at $50\%$ sparsity, COSTGRAD matches or exceeds full-token planning on three of four continuous-control benchmarks, while giving a measured $2.6\times$ wall-clock speedup per environment planning step. Combining token sparsity with reduced CEM search increases this to a $\sim 5\times$ total speedup while still exceeding the full-token baseline. We also identify an architecture-dependent failure mode: in a matched AdaLN-vs-concat comparison, concat maintains comparable full-token performance but pure COSTGRAD loses its advantage over random selection. This difference tracks action-pathway drift: gradient-selected removal produces less drift than random removal on AdaLN, but more on concat. These results highlight selector-architecture compatibility as a design axis for sparse world-model planning. Project page and demos: this https URL

---


### 272. [Active Inference for Interaction-Mediated Control of a High-Dimensional Robotic Arm](https://arxiv.org/abs/2610.10275)

**<font color=#1a73e8>作者：</font>** Fraser C. Paterson, Sebastian Stein, Markus Klar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We propose interaction-mediated control via Active Inference as a general architectural approach to high-dimensional control problems in Human--Computer Interaction (HCI). This architecture recasts user interaction as the provision of evidence about a latent task objective, rather than the direct specification of plant-control inputs. The mediating function is distributed between an interaction broker, which selects informative user queries and performs Bayesian inference over user preferences, and an Active Inference controller, which autonomously plans and acts under the resulting preference information to control the plant. This division of labour decouples the semantics of user interaction from those of low-level plant control. We instantiate the architecture in a simulated, multi-link robotic arm to perform a simultaneous whole-arm target-coverage task. A simulated user communicates exclusively through a clutch-style binary evaluative channel, without specifying joint-torque commands. Across increasing arm dimensionalities, the architecture achieves successful interaction-mediated control, although task success is lower than when the controller receives the true target preferences directly. Exact target-subset identification also remains imperfect, highlighting the distinction between preference inference and successful task completion. The experimental findings provide an initial computational demonstration of the proposed architecture under controlled, matched-model assumptions and motivate its further investigation in broader HCI applications.

---


### 273. [AI Safety Considerations for Agents With Limited Time to Act](https://arxiv.org/abs/2610.10285)

**<font color=#1a73e8>作者：</font>** Leo Zeitler, Jack Richings, Victoria Nockles  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In the wake of the increasingly public discussion about AI alignment, recent work has tried to propose specific AI architectures that behave safely. However, the proposed arguments that seemingly demonstrate proved alignment mostly neglect the environment the agent needs to act in. We discuss theoretical bounds for agent-agnostic safety guarantees in environments that can only be partially observed and within which an action is required within limited time. We introduce two realistic scenarios, one with an infinite state space and one with signal mixture. In these scenarios, we prove that even a perfect agent cannot guarantee safe behaviour. It will be argued that for any proof of AI safety or alignment, the environment and associated safe actions need to be specifically considered together with the agent.

---


### 274. [TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning](https://arxiv.org/abs/2610.10288)

**<font color=#1a73e8>作者：</font>** Dayou Li, Hao Wang, Qianqian Yang 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale egocentric human interaction data is becoming an important source of physical supervision for embodied learning, yet video alone leaves the contact and pressure that characterize physical interaction unrecorded. Recent visual-tactile datasets provide this missing supervision, but their synchronized tactile data remain far smaller in volume than human video. Moreover, the largest resources often merge recordings from different sensors or annotation procedures, which makes the effect of data scale difficult to isolate. We therefore introduce TouchScale, a 500-hour dataset of contact-rich human interaction recorded with a single unified wearable setup. Its approximately 2K predefined task descriptions span everyday activities and structured manipulation, and each recording temporally aligns egocentric RGB-D video with wrist RGB video and dense full-hand bimanual tactile measurements. Compared with prior tactile data, training on the full TouchScale raises zero-shot contact IoU on data from an unseen tactile sensor from 0.134 to 0.383. Pretraining a visual encoder on TouchScale also yields the highest action recognition accuracy on three benchmarks among the compared visual-tactile datasets. Used for visual-tactile mid-training of a robot policy, TouchScale improves the average real-world success rate across four contact-rich manipulation tasks from 22.5% to 57.5%. With the sensor and collection protocol held fixed, both zero-shot tactile prediction and robot success show an overall upward trend as more TouchScale data is used. These results suggest that human visual-tactile data collected at scale with consistent sensing benefits both perception and robot manipulation. We will publicly release TouchScale, including all synchronized visual-tactile recordings and reconstructed object models, to support future research on scalable visual-tactile learning.

---


### 275. [Physics-Aligned Electronic Ground-State Learning Improves Generalization](https://arxiv.org/abs/2610.10298)

**<font color=#1a73e8>作者：</font>** Eike S. Eberhard, Xaver Kainz, Viktor Kotsev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learned interatomic potentials (MLIPs) excel at in-distribution tasks, accelerating drug and material development, yet they struggle to generalize out-of-distribution. We propose to push the cost-accuracy Pareto frontier by designing observable-agnostic electronic ground-state descriptor models (GSMs) with computational costs situated between MLIPs and Kohn-Sham density functional theory (KS-DFT). We align the learning objectives and architectures of GSMs with the governing equations of KS-DFT by enforcing physical constraints and removing optimization pressure on unphysical or irrelevant degrees of freedom. In our size-extrapolation experiments from QM9 to QM40, our combined contributions OrthoNormal-Loss (ON-Loss) and Grassmann Restricted Occupied-Orbital Training (GROOT) reach a 79.1% energy and 83.4% force mean absolute error (MAE) reduction over previous state-of-the-art density GSMs. For Hamiltonian GSMs, ON-Loss and Residual Optimal-gauge Conditioning-aware KS-Eq. Training (ROCKET) together reduce the energy and force MAEs of the strongest baseline by 99.8% and 95.9%, respectively. Using a self-consistency rejection criterion, we filter out extrapolation errors on QMugs, rejecting fewer than 0.4% of predictions while reaching an energy MAE of 0.07 mHa. Finally, we demonstrate the efficiency of label-free self-consistency fine-tuning, and transfer GSMs to reactive chemistry in Transition1x, reaching energy errors below chemical accuracy.

---


### 276. [Shared Gaussianization: What Gaussian Regularizers Certify About Contrastive Learning, and What They Miss](https://arxiv.org/abs/2610.10299)

**<font color=#1a73e8>作者：</font>** Ruoyu Zhao, Yuting Chen, Jinheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What can a distribution-matching regularizer such as SIGReg in LeJEPA certify about contrastive learning? We study shared Gaussianization (SG), a characteristic-function Gaussianity test on the average of two normalized views, scaled by an independent $\chi_d$ radius. Because disagreeing views shorten the average, one test detects both misalignment and non-uniformity. SG vanishes exactly at the aligned, uniform minimizers of population InfoNCE, and under equal marginals it bounds the InfoNCE excess by $4\cdot 3^{3/4}\beta$ times the square root of the SG loss, plus a term linear in the loss. The square-root rate and this dimension-free constant are sharp, and no squared mean-embedding distance on view pairs achieves a faster rate. With an explicit alignment term, a rotation-invariant uniformity test gives a linear bound if and only if its spectrum dominates that of InfoNCE's kernel $e^{\beta u^\top v}$; SG's own test does, Gaussian kernels $e^{-\gamma \|u-v\|^2}$ qualify exactly when $\gamma \ge \beta/2$, and moment matching never does. Away from the optimum, the objectives differ. Along an isotropic nuisance channel, pure SG lowers its loss by adding per-view nuisance whenever the shared code is non-uniform. An alignment weight above the channel's gain makes the nuisance-free solution a strict local minimizer; for LeJEPA, the same rule gives a critical SIGReg weight that decreases with the batch size. At finite batch size, an off-diagonal U-statistic removes a plug-in bias toward misalignment. In controlled latent-variable models, pure SG retains per-view style, an alignment weight above the measured gain removes it, and for LeJEPA at three batch sizes the measured gain separates the encoders that retain style from those that do not. InfoNCE training also reaches a lower SG$_{0.2}$ loss than SG$_{0.2}$ training from scratch, which points to an optimization gap.

---


### 277. [Revisiting Explainable AI through Model-Independent Concept Dictionaries](https://arxiv.org/abs/2610.10301)

**<font color=#1a73e8>作者：</font>** Thomas Schnake, Doreen Schöppenthau, Alexander Meyer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern applications of AI rely on increasingly complex models. Explainable AI (XAI) has emerged as a set of techniques aimed at improving model transparency. However, existing XAI methods typically assume input features to be inherently interpretable, or they rely on intermediate internal abstractions that are difficult to characterize and highly architecture-specific, hindering consistent use across models. To address these limitations, we propose DictXAI, a method that defines concepts directly in the input domain via a dictionary---a large, potentially overcomplete set of predefined elements, each carrying an interpretable meaning. Technically, DictXAI first computes a sparse code of the input and then attributes the model's prediction to the associated dictionary elements. We demonstrate the actionable nature of DictXAI explanations, showing that they can attribute AI malfunctions (e.g., Clever Hans effects) directly to identifiable artifact patterns in the data, while fostering human-AI alignment on intricate biomedical signals. We further demonstrate our method's ability to operate across a wide variety of dictionaries, including learned image bases, analytically defined waveforms for electrocardiography, and experimentally acquired dictionary elements. Overall, our results show that DictXAI provides more interpretable, actionable, and architecture-agnostic insights than classical XAI or existing concept-based approaches.

---


### 278. [Continual Graph Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.10302)

**<font color=#1a73e8>作者：</font>** Tommaso Marzi, Ahmed Hendawy, Jan Peters 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Continual Multi-Agent Reinforcement Learning (CMARL), agents learn cooperative policies across sequences of tasks, aiming to adapt effectively to new tasks while preserving the ability to solve previously encountered ones. In many applications, tasks differ in their underlying structure, which can represent, for example, distinct operational conditions or target configurations (e.g., different network topologies in power grids or arrangements in formation control). Existing CMARL methods lack dedicated mechanisms to leverage this structural information when learning new tasks, failing to promote transfer and mitigate forgetting. To fill this gap, we propose Continual Graph Multi-Agent Reinforcement Learning (CGMARL), a novel framework for CMARL problems in which task sequences are mapped into a series of attributed graphs, each modeling a task-specific structure. In CGMARL, each graph determines the environment dynamics (next states and/or rewards) and the number of agents for the corresponding task. Then, we present Graph-based Formation (GRAFO), the first CGMARL benchmark, and show how forgetting arises in this setting. Finally, to address this limitation, we propose Frozen Graph Encoder (FROG), a method that relies on a frozen graph backbone to preserve past structural information in graph-based CMARL policies. Experiments on GRAFO show that pairing FROG with existing CL methods substantially improves performance on multiple CGMARL scenarios.

---


### 279. [On the Necessity of Attention-FFN Split in Vision Transformers](https://arxiv.org/abs/2610.10303)

**<font color=#1a73e8>作者：</font>** Junhyeok Kim, Jinyeong Kim, Jae Wan Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The standard Transformer architecture relies on a rigid pattern that alternates Attention and Feed-Forward Network (FFN) layers. Despite its widespread adoption, the inductive bias imposed by this strict separation has not been systematically examined. In this work, we investigate the necessity of the Attention-FFN dichotomy in Vision Transformers (ViTs). To facilitate this analysis, we introduce the AttenFeed module, a unified component that integrates the functional properties of both Attention and FFN. Based on this module, we devise the unified Vision Transformer (uViT), which replaces the conventional alternating Attention-FFN structure with a sequence of AttenFeed modules. We then use uViT as a control group that relaxes the Attention-FFN dichotomy of the standard ViT and systematically compare the two models across multiple datasets and model scales. Our experiments reveal that the Attention-FFN dichotomy can hinder performance at smaller model scales due to the rigid parameter allocation of ViTs. The AttenFeed module and uViT serve as new analytical tools for understanding the Attention-FFN structure and offer theoretical insights into the heuristically designed architecture of conventional ViTs.

---


### 280. [How Do Transformers Learn to Represent Symmetries?](https://arxiv.org/abs/2610.10305)

**<font color=#1a73e8>作者：</font>** Eduardo Santos-Escriche, Valerie Engelmayer, Ya-Wei Eileen Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training Transformer-based architectures with finite data augmentation has become an increasingly popular approach in geometric machine learning. Despite its empirical success, the interplay between the Transformer architecture, invariance to different symmetries, and augmentation budgets remains underexplored. In this paper, we study the ability of a vanilla Transformer to learn various symmetries through finite data augmentation for point cloud datasets. We identify an ordering of increasing learnability across the following symmetry groups: (i) non-angle-preserving symmetries, (ii) angle-preserving symmetries, and (iii) base angle-preserving subgroups, such as translation, rotation, and scale. For the base angle-preserving groups, we further investigate the Transformer's extrapolation behavior and conduct a structural analysis of the trained models, allowing us to identify interpretable mechanisms that induce invariance. Finally, we extend our analysis to equivariant functions and show that the detected mechanisms for approximate invariance can also provide a key building block for learned equivariance. Our project page is available at this https URL

---


### 281. [One-Shot Adaptive Segmentation For Scientific Images](https://arxiv.org/abs/2610.10306)

**<font color=#1a73e8>作者：</font>** Tejaswi V. Panchagnula, Allison M. Davis, Fengqing Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific image segmentation methods rely on extensive annotation and task-specific training, limiting adaptation across imaging modalities and experimental conditions. We present a training-free, one-shot framework that specializes vision foundation models using a single annotated reference image. The framework combines DINOv3 representations with background-adaptive feature orthogonalization to suppress artifact-related feature directions, after which cosine similarity localizes candidate regions for SAM segmentation. We evaluate the framework on red-blood-cell microscopy, structured-illumination pool boiling, and chest radiography. Relative to the strongest baseline, the proposed method improves mean IoU by 5.91% and 78.62% on the microscopy and pool-boiling datasets, respectively, while achieving comparable performance on chest radiographs. These results demonstrate that one-shot reference conditioning can adapt general-purpose vision models to specialized scientific segmentation tasks.

---


### 282. [RSIGym: A Flexible Environment for Recursive Self-Improvement](https://arxiv.org/abs/2610.10310)

**<font color=#1a73e8>作者：</font>** Fanqing Meng, Lingxiao Du, Haocheng Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement requires carrying accepted changes into later improvement cycles, while studying agent-proposed changes also requires substantial research infrastructure. Existing settings often leave agents to rebuild routine infrastructure or restrict exploration to individual components. We introduce RSIGym, an agent-native research environment based on Everything as a Service (EaaS). RSIGym exposes training, inference, rollout, evaluation, and sandbox execution through reusable services, with shared budget and permission controls supporting Data, Harness, and Joint improvement tracks. This design enables agents to investigate individual interventions and jointly optimize data, training settings, and execution harnesses within the same environment. We define RSI-Index as the mean fraction of the remaining performance gap closed across five benchmarks covering software engineering, terminal interaction, mathematics, scientific reasoning, and skill-based tasks. Comparing six frontier research models in independent Joint runs, Opus 5 achieves the highest RSI-Index of 0.4809 under a $500 platform-service budget per benchmark run. Its selected systems improve all five benchmarks, raising SWE-bench Verified from 17.67% to 50.33% and AIME from 31.67% to 97.78%. Additional experiments examine DSH-harness refinement, budget variation, and restricted network access, while recorded trajectories reveal how agents diagnose failures and select candidates. We open-source the full RSIGym codebase and results to support reproducibility and further research.

---


### 283. [PoreML: A Data-Driven Framework for Learning Multiphase Flow in Porous Media](https://arxiv.org/abs/2610.10314)

**<font color=#1a73e8>作者：</font>** Chunyang Wang, Mingrui Zhang, Yuyan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiphase flow in porous microstructures is central to CO$_2$ storage, fuel-cell operation, and flip-chip packaging. Predicting these flows remains challenging because wettability and complex pore geometry govern the nonlinear evolution of fluid interfaces. Machine learning holds substantial promise for advancing the field, but progress is constrained by scarce time-resolved 3D datasets and a lack of a unified workflow for training and evaluating models. To fill this critical gap, we introduce PoreML, an open-source framework unifying data generation, model training, and evaluation grounded in pore-scale physics. The framework comprises three core components. (a) A modern GPU-native lattice Boltzmann solver, validated against analytical solutions and published experiments, enables reproducible data generation. (b) A 3.3 TB dataset contains 560 simulation runs and 158,546 stored time steps across four application-driven scenarios. These trajectories span synthetic structures and geometries derived from micro-CT scans of real materials, covering diverse wetting conditions and viscosity ratios. (c) A unified learning framework evaluates one-step prediction and autoregressive rollouts. Its domain-specific evaluation protocols assess predictive accuracy and physical consistency. We evaluate five models of diverse architecture under these protocols. Two complementary challenges assess transfer to larger domains and from synthetic to micro-CT-derived structures. PoreML provides a shared foundation for machine-learning research on multiphase flow in porous media, with the aim of empowering the community to develop reliable predictive models and advance the field.

---


### 284. [From Digital Human Interactions to Physics-Based Humanoid Skills: Physics-Grounded Post-Training of Interaction Generators](https://arxiv.org/abs/2610.10322)

**<font color=#1a73e8>作者：</font>** Kerui Chen, Jianrong Zhang, Kai Lv 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent methods have made promising progress in generating interactions between two humanoids, largely relying on physics-based tracking policies to convert digital reference motions into executable trajectories. However, limited tracking capabilities restrict the range of reference motions that can be successfully executed, reducing data utilization. Moreover, even successful tracking does not guarantee physically plausible responses or faithful realization of the intended interactions. In this paper, we introduce DIGHT, a co-adaptive framework that couples a Digital human Interaction Generator with a Humanoid Tracking policy. Our DIGHT first executes multiple text-conditioned interaction candidates in simulation using a fixed tracker. It then constructs physics-grounded preferences from the resulting rollouts, covering both general executability and interaction fidelity. Rather than collapsing these signals into a single scalar reward for candidate ranking, we align the pretrained generator using physics-decoupled diffusion direct preference optimization (DPO), preserving criterion-specific supervision without differentiating through the simulator. To improve executability, preference pairs are derived from tracking error, friction, and floating. Additionally, to improve interaction fidelity, we propose to incorporate force feedback from simulator as a measure of contact fidelity and construct preferences over contact occurrence, location, duration, and force magnitude. The aligned generator then supplies reference motions for fine-tuning the tracker, improving compatibility between generation and physical execution. Extensive experiments demonstrate that our approach not only improves the physical plausibility of generated motions but also enables more reliable and faithful humanoid interactions in simulation.

---


### 285. [HAN-Mamba: Hierarchical Selective State Space Networks for Multi-Scale Financial Volatility Forecasting](https://arxiv.org/abs/2610.10323)

**<font color=#1a73e8>作者：</font>** Mihai Bogdan Deaconu, Ioan Daniel Pop  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short-horizon realized volatility forecasting requires the integration of market information that evolves at incompatible temporal resolutions, from second-level order book dynamics to weekly regime drift. Our conference work introduced HAN-T, a hierarchical architecture in which scale-specific Transformer encoders process short, mid, and long-horizon streams and a learned attention fuser weighs their contributions. This article replaces the quadratic attention encoders with selective state space (Mamba) encoders while retaining attention only in the fuser, where the input is a three-token set rather than a long sequence. The resulting hybrid, HAN-Mamba, summarizes each stream through a recurrent state whose input-dependent gating matches two structural properties of volatility: persistent but decaying memory and abrupt regime shifts. On the Optiver Realized Volatility Prediction benchmark under time-aware five-fold cross-validation, HAN-Mamba improves mean RMSPE over HAN-T (0.1942 vs. 0.1965) with 33% fewer parameters. Its linear-time encoders further allow the high-frequency context to be extended from 60 to 240 buckets, reducing error to 0.1927 where the attention variant saturates, and support constant-time streaming updates at inference. Ablations attribute the gains to the encoder swap, confirm that the hierarchical prior transfers across sequence-model families, and show that the permutation-invariant attention fuser remains the correct mechanism for cross-scale integration.

---


### 286. [Performance at What Cost? A Sustainability-Aware Performance Index for Cell and Nucleus Instance Segmentation](https://arxiv.org/abs/2610.10324)

**<font color=#1a73e8>作者：</font>** Eiram Mahera Sheikh, Alaa Tharwat, Wolfram Schenck  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained models for cell and nuclear instance segmentation differ substantially in architecture, pretraining data and objectives, parameter count, inference strategy, adaptation requirements, postprocessing pipeline, and computational demand. Large pretrained and foundation models are increasingly adopted because of their strong zero-shot capabilities, but their use also imposes greater energy consumption, memory requirements, computational demands, adaptation costs, and operational carbon emissions. Whether these additional demands are justified by meaningful gains in segmentation performance remains unclear. We address this question by introducing the Sustainability-Aware Performance Index (SAPI), a configurable metric that combines segmentation performance, energy consumption, and model size. We benchmark 19 pretrained and foundation models across six CellBinDB datasets under zero-shot inference and evaluate 16 fine-tunable models using few-shot adaptation with both frozen encoder and full-model fine-tuning. We estimate energy consumption for GPU, CPU, and RAM using software-based monitoring tools. Our results show that larger and more computationally demanding models do not consistently achieve proportionate improvements in segmentation quality. While few-shot adaptation benefits several models, the gains and resource costs vary considerably across architectures, datasets, and adaptation strategies, causing SAPI-based rankings to differ from rankings based on performance alone. This study provides a practical framework for comparing segmentation models more comprehensively and supports more computationally accessible and environmentally responsible model selection in biomedical image analysis.

---


### 287. [Average-Reward Reinforcement Learning for Multichain MDPs: A Hierarchical Decomposition Approach](https://arxiv.org/abs/2610.10326)

**<font color=#1a73e8>作者：</font>** Huizhen Yu, Isaiah Heidt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study learning optimal policies in average-reward multichain Markov decision processes (MDPs), where the optimal gain may depend on the initial state and recurrence structures vary across policies, creating challenges for reinforcement learning (RL) methods. We propose an asynchronous value-iteration-based RL algorithm that requires no model knowledge beyond the MDP's transition graph and leverages Bather's decomposition to hierarchically partition the state space into communicating subsystems and transient states. This decomposition induces a recasting of the global decision problem into structured subproblems, which our algorithm exploits. We show that the algorithm converges to the optimal gain and produces gain-optimal policies after finite time. Building on this base algorithm, we develop two further algorithms: one approximately solves the multichain average optimality equations to obtain near gain-optimal policies, and another targets near bias-optimality by approximating the optimal bias function and solving an induced average-reward multichain MDP using the base algorithm. We provide almost-sure convergence guarantees for all three algorithms and empirically compare their tradeoffs, showing that the latter two also consistently improve transient performance relative to the base algorithm. To our knowledge, these are the first essentially model-free average-reward RL algorithms for general multichain MDPs without reductions to discounted problems.

---


### 288. [Learning to Act with Task Progress: Distilling Small Agents from Compact Teacher Supervision](https://arxiv.org/abs/2610.10332)

**<font color=#1a73e8>作者：</font>** Wenxi Gan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Learning from large-model demonstrations offers a way to train small agents that can complete recurring tasks without calling a large model at every step. A central design choice is what to retain from teacher trajectories that contain reasoning, actions, and information about task progress. We introduce Task-Progress Distillation (TPD), an offline approach that pairs each demonstrated action with a short label describing the current task stage. The student learns these compact targets and selects actions by jointly scoring admissible stage--action pairs, which a deterministic harness executes in the environment. On ALFWorld, a 1.7B student trained with 404 demonstrations achieves 72.4\% mean unseen task success with either TPD or action-only supervision, compared with 48.3\% for a reasoning-trained student using constrained action selection. Explicit stages provide an additional benefit at 200 demonstrations, improving success from 48.0\% to 67.7\% over action-only supervision. With more demonstrations, the action-only student closes the gap, and both approaches reach 76.9\% at 808 demonstrations. Shared-history analyses link part of TPD's local advantage to better decisions when moving between subgoals, particularly from object acquisition to processing. These results show that compact supervision can train effective small task agents, while explicit task progress provides additional guidance at an intermediate demonstration budget.

---


### 289. [How Private is Private? A Comparative Study for Face De-Identification](https://arxiv.org/abs/2610.10334)

**<font color=#1a73e8>作者：</font>** Hui Wei, Hao Yu, Hui Kuurila-Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face de-identification (FDeID) has emerged as a critical privacy-preserving technology, yet its evaluation remains fundamentally fragmented. Existing protocols rely on inconsistent metrics, heterogeneous datasets, and partial annotation coverage, so methods targeting different utility dimensions, such as landmark versus expression preservation, are reported on different benchmarks under different metrics, rendering cross-method comparison infeasible. We revisit FDeID evaluation from both the data and metric perspectives. On the data side, we introduce UtilFace, a curated, demographically balanced benchmark with high identity diversity, assembled from four large-scale face datasets through identity-aware cleaning, resolution enhancement, and stratified filtering. On the metric side, we propose HiFD, a Hierarchical Face De-identification metric that unifies identity suppression, multi-level utility preservation, and image quality under a single consistency-based paradigm: every component is computed from pretrained estimators' outputs on the original face and its de-identified counterpart, directly quantifying how much identity is suppressed and how much downstream-perceivable utility survives. HiFD organizes facial signals into a three-level utility hierarchy spanning macro cues (L1), micro cues (L2), and imperceptible cues (L3), and aggregates the five resulting components into a single interpretable score via weighted harmonic mean, with configurable application-specific profiles. Using this unified protocol, we conduct a comprehensive comparative study spanning adversarial, GAN-based, and diffusion-based methods, surfacing trade-offs and failure modes that remain invisible under existing protocols. We release the benchmark and evaluation toolkit to foster systematic and reproducible research in privacy-preserving human face analysis.

---


### 290. [Position Forcing: Self-Conditioning 3D Generation](https://arxiv.org/abs/2610.10342)

**<font color=#1a73e8>作者：</font>** Ziheng Ouyang, Zeqiang Lai, Jiarui Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent single-stage 3D generative models commonly adopt VecSet representations, encoding 3D shapes as unordered sets of latent tokens. However, compared with two-stage methods that provide explicit positional guidance, these models must implicitly infer token positions throughout denoising, limiting their generation quality. We observe that, despite the absence of explicit positional conditioning, VecSet tokens retain recoverable spatial correspondences. Building on this observation, we propose Position Forcing, a position-based self-conditioning framework. During denoising, Position Forcing recovers token positions from the current clean latent estimate, quantizes them at progressively finer resolutions according to the denoising stage, and feeds the resulting positional encodings back into the diffusion Transformer. This progressively refined positional feedback provides spatial guidance at a granularity appropriate to each denoising stage, guiding shape generation along a coarse-to-fine trajectory and substantially improving generation quality without a separate position generation stage. Experiments demonstrate that Position Forcing achieves strong performance among single-stage 3D generative methods and outperforms several competitive multi-stage approaches.

---


### 291. [Real-Time Joint Audio-Video Generation by Parallel Adapter Composition](https://arxiv.org/abs/2610.10343)

**<font color=#1a73e8>作者：</font>** Jingyu Li, Xiaoxiao Xiang, Yiwen Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying a joint audio-video diffusion transformer for real-time, interactive generation normally requires two essential modifications: block-autoregressive attention, so frames can be emitted before the whole clip is finished, and few-step sampling, so each block is cheap. Conventionally, the streaming video literature obtains both capabilities from a chained pipeline. It first distills a bidirectional teacher into a causal student, then into a few-step one, or proceeds in reverse order. Each stage of such a chain fine-tunes the weights the previous one produced, so a later objective can undo an earlier capability. Following the idea of model merging, we show that on a packed audio-video backbone the two capabilities can be acquired in parallel. A causal adapter is trained against the frozen backbone, and an off-the-shelf few-step adapter provides the few-step capability. As the two edit different functional axes, we predict, and then verify, that their weight-update directions are near-orthogonal, without any explicit orthogonality constraint during training. Orthogonal updates should combine without interfering, so parallel composition is a direct sum. The two adapters are simply added at inference, with no joint training, yielding few-step, streaming audio-video whose image quality tracks the bidirectional teacher. Compared to the chained baselines, the composed model matches or beats them on most metrics, making parallel composition a practical approach. The resulting streaming system generates joint audio-video in real time, $\approx$26 fps at $480\times832$ without quantization, and sustains 30 s of continuous generation with stable image quality.

---


### 292. [The Handover Problem: Governing Autonomy Transitions in Human-AI Collaboration](https://arxiv.org/abs/2610.10352)

**<font color=#1a73e8>作者：</font>** Vicente Pelechano, Antoni Mestre, Manoli Albert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-machine systems rarely operate at a fixed level of AI autonomy. As operators and AI systems collaborate over time, control must shift: the AI can take on more responsibility when collaboration is stable, maintain its current role when evidence is ambiguous, or return control to the human when conditions deteriorate. Existing work on adaptive automation, supervisory control, trust in automation, and deskilling explains parts of this problem, but provides no auditable, multi-signal criterion for governing when autonomy should change across multi-cycle workflows.
We formalise this challenge as the Handover Problem: deciding, at each operational cycle, whether to escalate, maintain, or revert AI autonomy while keeping the process reversible, recoverable, and auditable. We introduce the Handover Readiness Score (HRS), a transparent composite measure that integrates four signal dimensions: operator readiness, human-AI trust, learning stability, and operational performance. It is combined with a hysteresis-based transition policy that requires sustained positive evidence before increasing autonomy but reverts promptly when conditions worsen.
Across software engineering and manufacturing domains, the HRS and hard safety guards address complementary failure regimes: guards enforce immediate corrective action when a single indicator breaches a critical threshold, while the HRS detects the slow, multi-signal erosion of operator readiness that no individual guard can observe. The framework establishes autonomy handover as a governance problem requiring explicit, composite, and auditable criteria. This provides a conceptual and formal foundation that adaptive automation research has not previously provided.

---


### 293. [Receiver-Domain Behavioral Probing for Backdoor-Resilient Federated GPS Spoofing Detection in UAV Networks](https://arxiv.org/abs/2610.10360)

**<font color=#1a73e8>作者：</font>** Will Jedrzejczak, Cole Walther, Dilpreet Gill 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning lets a UAV fleet train a shared GPS spoofing detector without raw receiver data leaving any aircraft, and several recent UAV-FL designs weight each client by the validation accuracy it reports about itself. We show this self-report is an exploitable attack lever: two compromised clients of ten that poison part of their data, scale their updates, and inflate their reported accuracy raise backdoor lift to +0.3036, higher than the same attack achieves without lying. We propose receiver-domain behavioral probing, in which the coordinator evaluates every submitted model on counterfactual spoofed samples built by driving each discriminative GPS feature to a benign value, weighting clients by what their models do rather than what they claim. Under independent and identically distributed clients this reduces attacker-induced lift to -0.0265, statistically indistinguishable from an honest fleet, while flagging the compromised aircraft. Unlike Byzantine-robust aggregation it needs no exact attacker count, only an honest majority: when the true count exceeds the configured value, Multi-Krum degrades from +0.0061 to +0.2837 while ours stays near baseline. Evaluation uses one public single-receiver dataset partitioned into simulated clients; we also report where the mechanism fails, under strong client heterogeneity.

---


### 294. [ORDERS: An Empirical Study of Norm-Rank Aggregation for Personalized Federated Learning](https://arxiv.org/abs/2610.10361)

**<font color=#1a73e8>作者：</font>** Koffka Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized federated learning combines shared representations with client-specific predictors, but the contribution of a server weighting rule can be obscured by local training and evaluation choices. We study ORDERS, a configuration that combines a shared backbone, a private residual adapter and classifier, geometric weights assigned by descending update norm, feature alignment, and private-parameter perturbations. The server computes a weighted sum of updates obtained from the same broadcast model; it does not obtain an additional optimization effect from sequential addition. A fully specified evaluation comprises 80 final runs: eight configurations, two datasets, and five training seeds on one fixed partition per dataset. On two-class-per-client CIFAR-10, ORDERS achieves $80.51 \pm 0.79\%$ native mean client accuracy, compared with $79.02 \pm 1.42\%$ for FedPer-R1 and $80.27 \pm 0.73\%$ for the matched uniform-weight control. After common local fine-tuning, the difference from FedPer-R1 narrows to 0.32 percentage points. On Sent140, ORDERS reaches $74.71 \pm 0.49\%$, only 0.69 points above a post hoc client training-majority diagnostic. Ablations provide limited, endpoint-dependent evidence for norm ranking and alignment, and no clear benefit from perturbations. Parameter-payload savings are 5.47% and 0.78%, respectively.

---


### 295. [Koopman Observers for Diffusion Acceleration: Correcting Feature Forecasts with Shallow Measurements](https://arxiv.org/abs/2610.10366)

**<font color=#1a73e8>作者：</font>** Hanru Bai, Yuanchao Xu, Fengyi Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature caching accelerates diffusion sampling by replacing expensive network evaluations with predictions from previously computed activations. However, forecasts based only on past features cannot directly incorporate changes in the current denoising state. We investigate whether inexpensive, freshly computed features can serve as observations for correcting these predictions. We introduce an observation-corrected Koopman framework for accelerating frozen diffusion models. Using calibration trajectories, we identify finite-dimensional, time-dependent Koopman approximations that jointly describe the increments of shallow and deep network features. During accelerated sampling, these operators predict the evolution of expensive deep features, while innovations in the observed shallow features correct the predicted state. Periodic full evaluations refresh the observer, and all generative-model parameters remain unchanged. This formulation enables controlled comparisons of temporal prediction and observation correction. Across three 10,000-image runs per dataset, our method reduces paired Inception-feature MSE by $19.9\%$ on CIFAR-10 and $11.9\%$ on a ten-class ImageNet subset relative to channelwise affine prediction under the same four-partial-step schedule. Matched ablations attribute additional reductions of $4.54\%$ and $4.67\%$ to observation correction. The observer achieves $1.89\times$ and $1.85\times$ measured speedups over DDIM-50, supporting improved reference-sampler fidelity without retraining the denoiser.

---


### 296. [Temporally Interpretable Differentiable Decision Trees](https://arxiv.org/abs/2610.10367)

**<font color=#1a73e8>作者：</font>** Eisuke Hirota, Aarav Sane, Rohan Paleja  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability offers a solution to safe autonomy by providing transparency into an agent's underlying decision-making model. Within sequential-decision making tasks, differentiable decision trees (DDTs) are one approach to such interpretability, maintaining automatic-differentiable policies while providing humans with a discrete tree-based visualization. Nonetheless, current implementations of DDTs are not well-suited for sequential-decision making domains, as there exists an inherent mismatch between a tree's single-timestep behavior and a human's multi-timestep planning. Our work thus introduces time as a new dimension of interpretability, coined as temporal interpretability, and demonstrates how temporal abstractions via action chunking improve it. We achieve this by first introducing two novel policy gradient algorithms that incorporate action chunking. Additionally, to maintain parameter-efficient trees, we develop an information-theoretic tree restructuring algorithm that modifies the tree during training. Across four simulation environments, we find that warm-starting action chunked DDTs from a distilled action chunked policy is the most effective way to obtain temporally interpretable trees: they match neural network policies in three of the four domains while using up to 80$\%$ fewer parameters. Our code is available at this https URL.

---


### 297. [PalmSpace: Towards a Versatile On-Palm Interaction Space through Unified Touch Modeling](https://arxiv.org/abs/2610.10370)

**<font color=#1a73e8>作者：</font>** Chentao Li, Mingze Gao, Runze Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As smart glasses and lightweight MR devices become increasingly practical, input remains a key challenge. The bare palm is an always-available, tactile, and proprioceptively accessible surface, but it has neither an explicit coordinate system nor embedded touch sensing. Prior on-palm systems typically expose isolated touch events, discrete regions, continuous trajectories, or task-specific gestures, limiting the palm's ability to support precise selection and gesture manipulation through a common input representation. We present PalmSpace, a wrist-worn infrared system that exposes mode-aware, body-referenced absolute input on the bare palm without per-user sensing calibration. At the interaction level, PalmSpace jointly represents contact occurrence, interaction mode, and palm-referenced absolute location; at the model level, it learns these coupled outputs through a shared real-time representation. In leave-one-participant-out evaluation with 17 participants, PalmSpace achieved 6.7 mm mean localization error, 98.9% contact detection accuracy, and 96.7% F1 for four-class interaction-state recognition. User studies further demonstrated absolute pointing and dragging, eyes-free digit input, and representative multi-finger controls including scrolling and pinch-based map manipulation. These results show that a morphologically variable bare palm can function as a transferable, mode-aware interaction surface.

---


### 298. [Continual Learning without Continual Training](https://arxiv.org/abs/2610.10379)

**<font color=#1a73e8>作者：</font>** Nikita Narayanan, Ritham Majumdarr, Sonali Parbhoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning requires models to adapt to new domains and new classes while retaining prior knowledge. Many existing methods rely on continued optimization, using regularization, replay, or parameter expansion to prevent new updates from overwriting previously learned knowledge. Instead, we propose replacing continual training with continual inference: a PFN-based model that is meta-trained, and then frozen, adapting to new classes only by extending an in-context evidence set. Our model, Latent Concept PFN, performs in-context Bayesian inference over a latent concept space that captures semantic structure shared across domains and classes. As each new domain or class arrives, exemplars are added to the memory; adaptation reflects updated posterior beliefs over latent concepts rather than gradient updates. No parameters are changed, reducing forgetting. The same method handles both domain and class incremental continual learning without task identity. Concept annotations are only used during meta-training, acting as a soft anchor on the latent space rather than a fixed bottleneck. Unlike fixed-vocabulary concept methods, the model also handles noisy, ambiguous, or incomplete annotations by combining concept labels with raw input evidence to discover distinctions beyond the predefined concept set. Experiments on class and domain incremental learning datasets demonstrate competitive continual learning performance while learning interpretable latent concepts.

---


### 299. [Boosting and the Expressive Power of Simple Weak Learners via the $γ$-VC Dimension](https://arxiv.org/abs/2610.10383)

**<font color=#1a73e8>作者：</font>** Arthur da Cunha, Kasper Green Larsen, Liang-Yu Zou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Boosting converts weak hypotheses with a small edge over random guessing into highly accurate predictors, but the expressive power of the resulting classifier can depend strongly on the structure of the base class. We study this phenomenon through the $\gamma$-VC dimension introduced by Alon et al. (STOC 2021). Our first result shows that this parameter characterizes the sample complexity for weak-to-strong learning up to a constant factor scaling in $\gamma$. We then sharpen the general relationship between the classic VC dimension and the $\gamma$-VC dimension. Finally, we also give improved upper and lower bounds on the $\gamma$-VC dimension for the fundamental concept classes of decision stumps and axis-parallel rectangles in $\mathbb{R}^d$.

---


### 300. [MOTIP2: Spatial Priors for End-to-End Multi-Object Tracking](https://arxiv.org/abs/2610.10391)

**<font color=#1a73e8>作者：</font>** Benoît Roussel, Damien Bouet, Liming Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end multi-object trackers have narrowed the gap with classical tracking-by-detection on association-difficult benchmarks. Yet they still make spatially implausible errors no classical tracker would, such as assigning one identity to objects on opposite sides of the frame. A model could learn to avoid them, but tracking annotations are scarce, so we encode spatial priors explicitly instead, while keeping inference fully end-to-end with no post-hoc association.
We propose three spatial priors, at the data, loss, and representation stages. Spatial ID Switches bias trajectory permutations toward spatially overlapping objects, reducing the mismatch between training and inference confusions. Spatial ID Loss scales each identity's penalty by its box distance, so a distant switch costs more than a nearby one. Spatial Anchor gives each track token its frame position, an explicit spatial cue for attention.
We instantiate the three priors in MOTIP2, a tracker adapted from MOTIP and built on the real-time DEIM detection transformer. Trained without extra data, its main model, MOTIP2-L, sets a new state of the art: 73.4 HOTA on DanceTrack, 76.0 on SportsMOT, and 71.1 IDF1 on PersonPath22. MOTIP2 is a family of models spanning the speed-accuracy trade-off: a lighter model, MOTIP2-S, matches the original MOTIP at over 3x the speed, and MOTIP2-X reaches 74.8 HOTA on DanceTrack.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-324](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
