# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 151. [[Re] Boosting the Visual Interpretability of CLIP via Adversarial Fine-Tuning](https://arxiv.org/abs/2610.14832)

**<font color=#1a73e8>作者：</font>** Anton Nuzhdin, Andrei Gruzitski, Balázs Egyed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a reproducibility study of ``Boosting the Visual Interpretability of CLIP via Adversarial Fine-Tuning'', published at ICLR 2025, which proposes an unsupervised adversarial fine-tuning (AFT) method with norm regularisation to enhance the visual interpretability of CLIP's image encoder. We attempt to reproduce the key claims regarding improved saliency map quality, increased concept alignment, transferability to out-of-distribution datasets, and the trade-off with zero-shot accuracy. Beyond reproduction, we propose a saliency-guided regularisation extension that introduces an Energy Pointing Game loss, directly supervising the spatial alignment of Simple Gradient saliency maps with target objects. We evaluate our extension across a range of saliency-loss weights and show that explicit saliency supervision \rev{substantially} improves localisation metrics at a modest cost: the reduction in zero-shot accuracy and adversarial robustness is small at the lowest saliency-loss weight ($w_s=0.2$) and moderate at the strongest setting ($w_s=0.6$). We restructure the codebase for configurable, systematic experimentation.

---


### 152. [Sequence-Structured Decision Learning for Branch-and-Bound in Mixed-Integer Linear Programming](https://arxiv.org/abs/2610.14835)

**<font color=#1a73e8>作者：</font>** Tengfei Liu, Jinrun Liu, Bai Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Branch-and-bound (BnB) solves mixed-integer linear programs by constructing and exploring a search tree. Node selection and branching are two recurrent decisions that directly determine the tree. Learning-based approaches typically optimize either decision in isolation and condition on a mostly local view, leaving the coupled evolution of the search tree insufficiently modeled. This paper proposes Seq-BnB, a sequence-structured framework that learns branching and node selection from a shared global representation of the evolving BnB process. Seq-BnB serializes node creations, node updates, node-selection events, and branching events into typed tokens, producing a causal event sequence of the search trajectory. A self-attention encoder summarizes this global search history, a bipartite graph neural network encodes the current LP relaxation, and context-conditioned decision heads score branching variables and open nodes. To reduce distribution shift between expert demonstrations and learned policies, Seq-BnB is trained with DAgger-style data aggregation. On four MILP benchmark families, Seq-BnB consistently processes fewer BnB nodes than heuristic and learning-based baselines, with strong solution times on both standard and larger transfer instances. While this paper evaluates Seq-BnB instantiation for branching and node selection, it accommodates additional solver decisions, such as cut selection, by introducing new action tokens and decision heads.

---


### 153. [Pre-Registered Genesis Accounting for Recursive Self-Improvement: First Audited Operator-Genesis Events in a Physics-Discovery Runtime](https://arxiv.org/abs/2610.14843)

**<font color=#1a73e8>作者：</font>** Wenbin Mao, Pei Zou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Claims of recursive self-improvement are easy to make and hard to falsify: did improvement come from re-using designer-provided mechanisms, or from mechanisms the system authored itself? We introduce a pre-registered, two-tier accounting: M1 counts machine-generated content instances within a designer-provided vocabulary, while M2 counts machine-authored mechanism types (new operators registered into the runtime's own vocabulary, with a held-out-validation certificate). We report the first audited M2 genesis events. In the primary event, depth-limited compositional search over elementary operators, judged by held-out R^2 on real NIST hydrogen Balmer measurements, produced the operator sq(inv(n)) = 1/n^2 -- the Rydberg-level form -- which no standard-library transform could express (held-out R^2: -0.546 best standard transform vs. 1.0000000 composed). A protocol flaw (independent variable built by inverting the very law under test) was caught in audit and repaired via an independent-label protocol; extrapolation to unseen levels (n=8,9 trained on n<=7) attains relative error ~10^-6, four to six orders beyond the best standard operator. A second event independently recovered sqrt(inv(a)) -- Kepler's velocity law -- from JPL ephemeris vectors. Also incorporated: an audited compounding channel (first domain-level measurement: 1.109x accuracy ratio on a real held-out domain) and blind, decurated genesis exams whose honest tally is zero. The Kepler event passes line audit; the hydrogen gap reproduces on He II; the certificate is threshold-stable. Against eleven prior systems, the contribution is the measurement and governance of machine-authored mechanisms, not the search algorithm or rediscovered physics. Limitations: exams were curated by agents who knew the textbook answer, triggers manual, grammar observer-injected; both events demonstrate capability to author, not yet autonomous genesis.

---


### 154. [Towards Privacy-Preserving Thermal Human Perception from Dataset to Deployment](https://arxiv.org/abs/2610.14846)

**<font color=#1a73e8>作者：</font>** Kailai Sun, Yue Cui, Xinwei Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Indoor human perception is the foundation for smart homes and healthcare. However, RGB cameras raise privacy concerns in private indoor environments, while low-resolution thermal cameras provide limited spatial and semantic information. Large-scale indoor thermal datasets and real-world deployments remain limited. Here, we introduce Indoor RGB-T, a large-scale paired RGB--thermal dataset for indoor human perception. The dataset covers 20 indoor rooms and contains 90,576 80x62 thermal frames, 87,016 temporally matched RGB--thermal pairs, and 115,557 annotated human bounding boxes. We establish benchmarks for robust thermal occupant-state detection with 0.75 mAP and occupancy estimation with an accuracy of 0.847 in unseen rooms. We further evaluate RGB-to-thermal and thermal-to-RGB translation, achieving a temperature MAE of 0.654 C and an R2 of 0.923. Finally, we deploy the thermal perception model on a commercial sleep-monitoring system in the real world. Field testing with 100 participants and deployment of approximately 1,000 devices further demonstrate its practical feasibility. We identify practical challenges that motivate future research directions, including environmental thermal interference, sensing range and multi-person occlusion. The code, trained models and partial dataset are available at this https URL and this https URL.

---


### 155. [StateSync-GKR: Design and Evaluation of a Reusable Sparse GKR Engine](https://arxiv.org/abs/2610.14849)

**<font color=#1a73e8>作者：</font>** Jinwook Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Authenticated state transitions need proof engines that conserve memory, avoid repeated setup, and preserve request semantics across parallel execution. We present StateSync-GKR, a reusable Rust sumcheck/GKR core with a sparse-Merkle frontend, and connect its design mechanisms to controlled measurements. Sparse layer reduction and derived wiring reduce prover ownership and repeated verification work. Cube/affine fusion and parallel path constraints keep the circuit schedule and proof-size growth compact. Reusable preparation and indexed parallel jobs amortize setup while maintaining independent results. Three-state records, strict original-request decoding, and separate core/model interfaces expose the application and assurance boundaries. With circuit, field, transcript and prover driver held fixed, sparse reduction lowers additional requested allocation 3,242-fold and peak process resident memory 89.46-fold relative to StateSync-GKR's test-only dense reference for a two-layer mixed circuit of width 4096. Direct depth-24 fresh/prepared measurements show 3.46-4.45-fold lower per-request proving-path latency. CPU and full-proof delivery studies distinguish useful parallel work from queueing and return-path costs, retaining all outcomes and latency budgets. The evaluation supports larger circuits within finite RAM, lower repeated-request cost, and explicit deployment choices for this artifact. It preserves the cryptographic claim boundary of the existing construction.

---


### 156. [Disentangling Marginal Capacity from Geometry in Optimal-Transport Label Transfer](https://arxiv.org/abs/2610.14853)

**<font color=#1a73e8>作者：</font>** Ali Khodabandeh Yalabadi, Azim Dehghani Amirabad, Artem Moskalev 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal transport (OT) is widely used to align distributions and transfer labels between unpaired source and target data, but source-target composition shifts can cause rare classes to be systematically under-predicted even with high transport confidence. We identify a source of this failure in the transport marginal: under the standard uniform weighting of source points, each class has transport capacity proportional to its source frequency, which can be insufficient to meet its target demand even when separated well in the embedding space. We show that displaced mass is preferentially absorbed by high-capacity classes rather than geometrically similar classes, producing confident errors that are difficult to detect from the transport plan. Downstream read-outs, entropic smoothing, and marginal relaxation provide limited recovery, whereas matching the transport marginal to the target composition substantially improves label transfer. On single-cell data, the oracle composition-matched marginal raises macro-F1 from 0.322 to 0.623, and the best deployable estimator closes 69% of the oracle gap. Correcting the marginal also separates a coverage-dependent component of error from residual error associated with class separability, showing that transport capacity and representation geometry are distinct sources of transfer error.

---


### 157. [CAST: Real-Time Motion Capture for Any Skeleton Topology](https://arxiv.org/abs/2610.14856)

**<font color=#1a73e8>作者：</font>** Pu Pang, Zhongfei Qing, Ling-Hao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies the problem of recovering motion from monocular video, even when the target skeleton topology differs from the subject observed in the video. Although previous methods have made efforts to resolve this problem, they remain vulnerable to joint-rotation errors that are coupled across the skeleton and can propagate along its kinematic hierarchy. To mitigate these errors, we present CAST, a topology-aware motion capture framework that combines learned local rotations with geometric correction guided by predicted global bone directions. Our observability analysis characterizes which rotational components can be constrained by outgoing bone directions. Guided by this analysis, GRACE uses reliability-gated alignment to correct composed orientations in parent-to-child order, leaving unconstrained components to the learned rotation predictor. The motion predictor and correction module are trained jointly with motion-derived supervision, using a frozen image encoder. Experiments under the TopoCap evaluation protocol show that the proposed framework improves motion recovery across different target topologies, including unseen structures. Reference-based cross-skeleton evaluation on a curated Mixamo benchmark and a user preference study further assess transfer to different target structures. A causal CAST-B variant achieves over 51 FPS on a single NVIDIA A100 GPU, with timing covering image encoding and motion prediction. Code repository: this https URL.

---


### 158. [World2TS: Real-World Event Context for Time-Series Forecasting](https://arxiv.org/abs/2610.14861)

**<font color=#1a73e8>作者：</font>** Zhiding Liu, Jiqian Yang, Mingyue Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting plays a vital role in a wide range of real-world applications. Recent approaches have achieved strong performance by modeling temporal correlations and cross-channel dependencies, yet most forecasting benchmarks still represent time series primarily as numerical histories. In practice, time series are observations of complex real-world processes, and their trajectories may reflect events, interventions, disruptions, and changes in measurement or reporting that cannot always be inferred from past values alone. A central barrier to studying context-aware forecasting is therefore the lack of large-scale datasets that align real-world events with the individual series they affect. We present World2TS, a scalable construction framework and large-scale dataset for time-series forecasting with real-world event context. We first develop world2ts-core, a reusable tool that combines agent-led semantic reasoning and Web search, command-line execution and validation, and human review within a feedback-driven discovery workflow. Given heterogeneous time series with semantic descriptions, the workflow discovers candidate events, consolidates retrieved evidence into verified events, and links them to relevant series under explicit temporal and semantic scopes. Using this framework, we construct world2ts-data, which contains 31 datasets across six domains, comprising 4,179 series, 97.1 million observations, 1,159 events, and 56,846 event-series links. We further conduct extensive data analyses and controlled comparative experiments to characterize the dataset and demonstrate the utility of the collected context for improving forecasting accuracy. World2TS provides a reusable data foundation for developing and evaluating context-aware forecasting models and agents. The project homepage is available at this https URL.

---


### 159. [Blending experimental electron density information to protein-ligand interaction](https://arxiv.org/abs/2610.14862)

**<font color=#1a73e8>作者：</font>** Seonghyun Park, Shuan Chen, Jun Jin Choong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models for protein-ligand interactions commonly rely on atomic coordinates, which are constructed by fitting molecular models to experimental electron-density maps. However, most models represent each complex as a single fitted structure, which can omit information about conformational heterogeneity, positional uncertainty, and local density support for individual atoms at binding interfaces. To fill this gap, we present CoDE, a Coordinate and Density Encoder, pre-trained on experimental density maps. We represent each binding site on a shared three-dimensional voxel grid combining atomic occupancy, experimental electron density, and its gradient magnitude. Using approximately 100K curated complexes, we pre-train a channel-wise vision transformer to jointly reconstruct masked atomic and density channels, learning a representation that integrates structural and experimental information. We evaluate the frozen encoder on two downstream tasks: (i) binding-affinity regression under leakage-controlled splits and (ii) pocket-conditioned ligand generation. Across these settings, CoDE improves over an identically pre-trained coordinate-only encoder and remains competitive with task-specific baselines, showing that density complements fitted atomic coordinates for protein-ligand interaction modeling and that the density-blended representation is useful for structure-based ligand generation.

---


### 160. [WeatherBridge: Forecast-Aware Multi-Source Input Adaptation for Pretrained Weather Forecasting Models](https://arxiv.org/abs/2610.14863)

**<font color=#1a73e8>作者：</font>** Mutian Xi, Xinyu Su, Xiaohui Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data-driven weather forecasting models are commonly trained on ERA5, yet operational deployment must use timely initial states from physics-based numerical weather prediction (NWP) systems whose distributions differ substantially from ERA5. Direct initialization with these states can degrade autoregressive forecasts, motivating input adaptation that keeps the pretrained forecasting model unchanged. Here, we introduce WeatherBridge, a unified, source-conditioned adapter that maps heterogeneous operational NWP initial states to ERA5 reference states without updating the pretrained forecasting model. WeatherBridge predicts the structured residual corrections with a Swin-UNet and injects source embeddings across multiple spatial scales, allowing the model to capture shared atmospheric structure and source-specific discrepancies. Its training objective combines latitude-weighted ERA5 reconstruction with One-step Rollout Alignment (ORA), which backpropagates one-step forecast error through a frozen FuXi model to optimize the adapted states for both initial state fidelity and downstream forecast compatibility. We evaluate WeatherBridge using daily GFS, HRES, and CMA initializations from 1 January to 22 November 2025 across six variables and lead times up to 240 hours. Relative to raw source initialization of FuXi, WeatherBridge reduces the mean RMSE of FuXi over the 6- 240-hour rollout for 17 of 18 source-variable combinations, with a median reduction of 10.2% and a maximum reduction of 46.3%. The adapter trained with frozen FuXi also improves FengWu forecasts on GFS inputs without retraining either the adapter or FengWu. These results demonstrate that forecast-aware input adaptation can improve forecasts from heterogeneous operational NWP inputs and transfer across pretrained ERA5-based forecasting models.

---


### 161. [ScalLoc: Continuous Oblique Thermal UAV Geo-Localization with a 2D Satellite Map](https://arxiv.org/abs/2610.14866)

**<font color=#1a73e8>作者：</font>** Xiaoran Zhang, Yu Liu, Jinyu Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal Thermal Geo-localization (TG) provides an illumination-robust positioning solution for Unmanned Aerial Vehicles (UAVs) in Global Navigation Satellite System (GNSS)-denied environments. However, existing thermal geo-localization methods mainly focus on near-nadir observations or depend on map-side elevation priors, limiting their applicability to continuous oblique thermal localization with only geo-referenced 2D satellite maps. To address this problem, we propose ScalLoc, a scale-aligned local-to-map localization framework for continuous oblique thermal UAV geo-localization. ScalLoc follows a reconstruction--refinement--anchoring--propagation design: it reconstructs local window geometry from thermal sequences, refines camera poses using track-based pose optimization, adaptively anchors each window to the satellite map, and propagates validated states to recover frame-level global trajectories. To support systematic evaluation, we construct Thermal-Oblique, a real thermal UAV sequence dataset containing 216 urban and rural day--night trajectories and 28,112 thermal frames with frame-level annotations. Extensive experiments demonstrate that ScalLoc reduces the mean localization error from 112.69 m to 26.97 m compared with the VGGT-only configuration, corresponding to a 76.07% reduction, and achieves the lowest frame-weighted mean position error among the compared methods. These results demonstrate the feasibility of continuous oblique thermal geo-localization using only lightweight 2D satellite maps, without requiring digital surface models or preconstructed 3D maps. Code and dataset are available at this https URL.

---


### 162. [MORE: Learning Motion-Oriented Registers for Driving World Models and Planning](https://arxiv.org/abs/2610.14871)

**<font color=#1a73e8>作者：</font>** Yingdong Gu, Haoyu Wang, Shaocheng Yan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> By predicting future states, latent world models provide rich self-supervision for end-to-end driving, but often inherit dense features from pretrained visual encoders as their world-state interface. This creates a mismatch: visual pretraining produces information-rich, spatially dense features, but their adaptation for motion-conditioned world modeling and planning is deferred to downstream training. The dense grid also makes future prediction more computationally expensive as visual resolution increases. We therefore argue that video pretraining should directly learn state representations suited to downstream world modeling and planning, rather than relying on downstream training to adapt inherited visual features. We propose ***MORE***, a V-JEPA framework that learns **M**otion-**O**riented **RE**gisters during video pretraining as a shared state interface for driving world models and planning. MORE injects temporally aligned ego motion into a small set of registers and uses them as the sole context for masked patch prediction, channeling dense patch-level supervision through a compact state bottleneck. A complementary blockwise register-masking objective further shapes predictive structure in the register space. During downstream training, the same register space defines the future states predicted by the world model and provides shared scene memory for trajectory generation and scoring. On NAVSIM-v2, MORE outperforms the state of the art by 1.6 in EPDMS, while achieving superior efficiency with only 1/10 the inference latency of DriveLaW. These results support learning the state interface for world modeling and planning directly during video pretraining.

---


### 163. [Contrastive Linearized Laplace: Loss Geometry, Valid Repairs, and Reliable Cores](https://arxiv.org/abs/2610.14875)

**<font color=#1a73e8>作者：</font>** Francisco J. Sáez-Maldonado, Luis A. Ortega, Andrés R. Masegosa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While contrastive learning is widely used to learn deterministic representations, it does not inherently provide estimates of uncertainty. Post-hoc uncertainty estimation methods, such as the Linearized Laplace approximation (LLA), offer a way to quantify uncertainty without retraining the encoder. However, we show that directly using the LLA induced distribution over the contrastive embedding does not yield reliable pointwise uncertainty estimates for downstream tasks: embedding variance alone does not reflect whether decisions such as nearest-neighbor retrieval or cluster assignment are stable. To address this limitation, we develop a post-hoc framework based on LLA that propagates encoder uncertainty through the downstream task. We characterize the curvature of contrastive objectives and introduce positive-semidefinite repairs where needed to obtain valid local Gaussian approximations without retraining the encoder. We test the proposed approach in metagenomic binning and image classification tasks. For metagenomic binning, posterior coassignment probabilities support consensus partitions and the selection of reliable cores, leading to improvements over existing baselines. Additional image classification experiments show calibration improvements on standard benchmarks and real histopathology datasets.

---


### 164. [Agent-Guided Evidence Acquisition for Emotion-Cause Pair Extraction](https://arxiv.org/abs/2610.14886)

**<font color=#1a73e8>作者：</font>** Zhuangzhuang Pan, Yan Xia, Chee Seng Chan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion-Cause Pair Extraction (ECPE) requires identifying the causes associated with emotions expressed in a conversation. Accurate extraction can depend on evidence that is not initially available, making it important to decide when further information is worth acquiring. We study agent-guided evidence acquisition for ECPE, where a student agent selectively accesses expert judgments for borderline relations on both sides of its validation-selected F1 decision boundary and revises only queried predictions. Through controlled comparisons under different information-access conditions, we examine how delegation granularity, query selection, and response integration affect prediction quality. At a nominal 10% query rate, selective fusion improves mean pair F1 by 2.64-3.88 points over the student in our main experiments, reaching 65.14 on ECF and 49.74 on MEC4 across model families. Our analysis suggests that greater access does not always translate into better cause identification. These findings motivate acquisition strategies that consider both the relevance of newly available evidence and its effect on prediction revision, providing an empirical basis for more effective and efficient evidence acquisition in ECPE.

---


### 165. [Pro-t-VAE: Closed-Form Student's t Mixtures for Robust Prototype Discovery](https://arxiv.org/abs/2610.14894)

**<font color=#1a73e8>作者：</font>** Zhikang Xu, Jiarui Xing, Jian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a robust deep generative framework for unsupervised image prototype discovery, built on a heavy-tailed Student's t mixture prior, that bridges statistical robustness and mathematical tractability. Existing generative approaches typically rely on noise-prone Gaussian priors or computationally intensive diffusion models; neither simultaneously provides explicit latent structure nor exact analytic optimization. While diffusion models can yield strong priors, iterative sampling and intractable likelihoods limit scalability and interpretability for prototype discovery. We address these issues by constructing a Student's t latent space via a Bayesian scale-mixture formulation. This yields a fully closed-form augmented ELBO for unsupervised Student's t mixture variational autoencoders, which, to our knowledge, is the first such objective applied to robust image prototype discovery, avoiding biased variational approximations and high computational costs in prior heavy-tailed or diffusion-based frameworks. Treating precision as a latent variable automatically modulates each data point's influence, downweighting outliers to learn a data-dependent measure of trust. The result is improved robustness, accuracy, and efficiency, with well-separated latent representations and more stable manifold learning than state-of-the-art methods. We validate our model on standard vision benchmarks and challenging neuroimaging tasks. In brain MRI-driven neurodegenerative disease analysis, our model recovers clean, anatomically coherent prototypes where clinical noise often collapses rare subtypes. These results highlight the ability of our framework to preserve anatomy-associated patterns for precise discovery in clinical settings. Our code is available at: this https URL.

---


### 166. [Prediction with Expert Advice under Heavy-Tailed Losses](https://arxiv.org/abs/2610.14904)

**<font color=#1a73e8>作者：</font>** Yuki Shibukawa, Shinji Ito  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study prediction with expert advice over $T$ rounds with $K$ experts under heavy-tailed losses whose $(1+\epsilon)$-moment is bounded by $\theta>0$ for some $\epsilon\in(0,1]$. In this setting, existing algorithms designed for the case $\epsilon=1$ can be suboptimal when $\epsilon<1$, suffering an additional polynomial dependence on $K$. We characterize the minimax pseudo-regret rate as $\Theta((\theta T)^{\frac{1}{1+\epsilon}}(\log K)^{\frac{\epsilon}{1+\epsilon}})$ and establish gap-dependent lower bounds in a self-bounded environment. To attain this minimax rate without prior knowledge of either $\epsilon$ or $\theta$, we propose Adaptive Heavy-Tailed FTRL, which uses robust data-dependent scale adaptation together with truncation. We further develop Adaptive Heavy-Tailed OMD, which likewise requires neither $\epsilon$ nor $\theta$ and achieves near-optimal regret guarantees in both adversarial and self-bounded environments. Finally, when $\epsilon$ and $\theta$ are known, an FTRL algorithm with Shannon-entropy regularization achieves optimal regret guarantees in both environments.

---


### 167. [Engram Neuron Inspired Adaptive Memorization for Lifelong Learning](https://arxiv.org/abs/2610.14940)

**<font color=#1a73e8>作者：</font>** Suiyang Jiang, Bomin Wang, Hangqi Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lifelong learning enables artificial systems to adapt to changing environments. To achieve this, an effective artificial learner should dynamically reorganize past and new experiences, maintaining stability while enabling flexible knowledge integration. However, existing efforts primarily mitigate catastrophic forgetting, lacking the ability to adaptively update memory akin to biological systems. Here, by integrating the full memory life cycle of engram neurons into artificial learners, we propose a framework that constructs a structured memory from gradient representations, which regulates parameter updates and guides memory management. Through comprehensive evaluations on four benchmarks, our approach shows promising lifelong learning capability, maintaining stability over long task sequences and supporting flexible adaptation. Beyond the performance gains, our approach offers a computational perspective on robust and flexible lifelong learning, echoing mechanisms observed in biological memory systems.

---


### 168. [Compositional Average Velocity Modeling for Efficient Diffusion Offline Reinforcement Learning](https://arxiv.org/abs/2610.14941)

**<font color=#1a73e8>作者：</font>** Thanh Nguyen, Abu Hanif Muhammad Syarubany, Hwanhee Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based policies have recently emerged as a powerful paradigm for offline reinforcement learning, but their reliance on multi-step denoising introduces substantial computational overhead and requires backpropagation through time during training, limiting scalability and practical deployment. In this work, we propose \textbf{Instant Flow Q-Learning (InsQL)}, a single-step generative policy learning framework that retains the expressive capacity of diffusion models while eliminating iterative sampling and BPTT. InsQL builds on the flow-matching perspective of diffusion policies, but replaces marginal velocity parameterization with \emph{average-velocity} modeling and introduces a principled compositional mechanism, yielding a theoretically grounded objective that learns average velocity consistently across scales. This formulation provides a direct noise-to-action mapping and enables single-step action generation. InsQL further unifies compositional average-velocity modeling with behavior-regularized actor--critic optimization in a single framework, requiring only a single policy network and avoiding distillation, multi-stage procedures, and Jacobian computations during training. At inference time, actions are generated in a single forward pass and can be refined via value-guided candidate selection to improve performance. Extensive experiments on standard offline RL benchmarks and real-world robotic manipulation tasks show that InsQL matches or surpasses state-of-the-art diffusion-based methods while substantially reducing both training and inference time. Overall, these results establish compositional average-velocity modeling as an efficient and scalable alternative to multi-step generative policies for offline RL.

---


### 169. [Probabilistic Multi-Source Data Selection via Learnable Categorical Priors: Variance Reduction and Guaranteed Derandomization](https://arxiv.org/abs/2610.14942)

**<font color=#1a73e8>作者：</font>** Shizhan Cai, Qixin Zhang, Siyuan Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bilevel data selection is a fundamental task with numerous applications in machine learning and statistics. A common strategy for tackling this problem is to relax the original bilevel combinatorial optimization into a continuous one. However, existing methods, including 0-1 relaxation and probabilistic relaxation, still suffer from several limitations, such as unstable gradient estimation and infeasible rounding. To address these issues, this paper proposes a new probabilistic relaxation for the multi-source bilevel data selection problem. Our key idea is to introduce multiple learnable categorical priors to parameterize a probability distribution supported only on feasible data subsets, thus naturally yielding a lossless rounding scheme. We further show that our proposed relaxation admits an effective two-point gradient estimator, which can simultaneously avoid the inverse-Hessian computation required by existing 0-1 relaxation and the unbounded score term appearing in prior probabilistic relaxation. Furthermore, we develop a reducible representation of this estimator, which substantially reduces the number of lower-level retrainings required for gradient computation. Built upon this reducible two-point estimator, we then design a novel stochastic gradient algorithm, termed ReSGD, for multi-source bilevel data selection problem, and establish a rigorous approximation guarantee for the subset returned by ReSGD under weak submodularity. Finally, extensive experiments are conducted to validate the effectiveness of our proposed ReSGD.

---


### 170. [Text-Guided Medical Image Segmentation via Residual Aggregation and Dense Alignment Representations](https://arxiv.org/abs/2610.14944)

**<font color=#1a73e8>作者：</font>** Jie Gui, Hang Tu, Yunfeng Dou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Specifying segmentation targets with natural language provides flexible semantic conditioning for medical image segmentation. However, existing methods still struggle to reliably ground high-level textual semantics into accurate pixel-level spatial prompts, especially under low-contrast lesions, ambiguous boundaries, and visually similar anatomical contexts. In this paper, we propose RADAR (Residual Aggregation and Dense Alignment Representations), a parameter-efficient framework for text-guided medical image segmentation. RADAR explicitly decouples and synergizes the medical semantic anchoring capability of BiomedCLIP with the prompt-driven mask decoding ability of MedSAM2, while enabling low-cost task adaptation via LoRA. Specifically, Guided Residual Depth Aggregation adaptively aggregates cross-layer features under semantic guidance to alleviate delayed textual injection and deep semantic dilution. Structured Dense Representation Alignment leverages a frozen BiomedCLIP to construct crop-level target, boundary, and context anchors, improving the local discriminability of dense features and the reliability of automatic prompts. Multi-modal Prompt Generation further converts cross-modal semantic responses into composite text, point, and mask prompts for MedSAM2 decoding. Experiments on three public medical image segmentation datasets show that RADAR achieves competitive performance with only 0.74M trainable parameters, demonstrating its effectiveness in parameter-efficient adaptation, semantic grounding, and dense representation enhancement. The source code is available at this https URL.

---


### 171. [DSM-Free UAV Visual Localization via Latent-Depth Variable Projection and Structure-Adaptive Coupling](https://arxiv.org/abs/2610.14945)

**<font color=#1a73e8>作者：</font>** Yibin Ye, Xichao Teng, Shuo Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual localization enables unmanned aerial vehicles (UAVs) to maintain absolute positioning in GNSS-denied environments. A common approach matches UAV images with geo-tagged orthographic maps and estimates camera pose using Perspective-n-Point (PnP) with elevations from Digital Surface Models (DSMs). However, accurate and up-to-date DSMs are often unavailable in practice. Orthographic-perspective geometry (OPG) enables DSM-free localization in scenes with varying elevations, yet existing methods typically estimate pose indirectly through intermediate matrix estimation and decomposition. To address this limitation, we propose Latent-Depth Variable Projection (LDVP), which treats the unknown scales along perspective viewing rays as latent depths. By analytically eliminating these depths and solving for the horizontal camera center in closed form given the rotation, LDVP reduces nonlinear estimation to a rotation-only problem, enabling direct recovery of metric horizontal position without assuming a planar scene. To improve localization robustness across different scene structures, we further introduce Structure-Adaptive Coupling (SAC), which uses relative scene structure inferred from monocular depth estimation to select LDVP when the matched points are not dominated by a single plane, and Planar-PnP otherwise. Our local observability analysis reveals how scene elevation variation affects the geometric constraints of OPG, providing a basis for this adaptive strategy. Extensive experiments show that LDVP consistently outperforms existing OPG-based DSM-free methods, while SAC further improves robustness across diverse scenes and substantially narrows the gap to DSM-based localization. Code will be released at this https URL.

---


### 172. [Exact Phase-Type Point Processes for Certified Measurement and Prediction of Event Streams](https://arxiv.org/abs/2610.14948)

**<font color=#1a73e8>作者：</font>** Sayak Dutta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal point processes are used both to measure market mechanisms, for example how fast prices absorb news and how much of the reaction is the market responding to itself, and to predict the next event. We show that one algebraic object, the phase-type (Erlang-chain) state space, serves both purposes with exact likelihoods. For measurement, we build a multiscale phase-type Hawkes process whose parameters all enter linearly. Its log-likelihood is concave, and we compute the global maximum together with a Fenchel duality-gap certificate. A Markov embedding gives the response to an exogenous shock, echoes included, in closed form, and this response is stable if and only if the spectral radius of the branching matrix is below one. Applied to six markets around 670 scheduled macroeconomic releases (2022-2026) with a built-in placebo test, the model shows that the direct reaction to CPI, payrolls, PPI and the FOMC statement is absorbed in about a second, while the market's own echoes stretch half of the response to 16-137 s. For prediction, we introduce EPT-X, a neural point process that adds a history-dependent mixture-of-Erlang renewal channel to a linear Hawkes backbone. Its intensity and compensator remain in closed form, its states follow an affine recursion that trains with a parallel scan, and it can start from the certified fit of the measurement model. EPT-X has the best test likelihood on all five LOBSTER order-book streams and on Retweet and Taobao, and is level with the best published model on StackOverflow. We also find that the EasyTPP implementation of IntensityFree clamps short inter-event times before scoring, and that the gaps of the EasyTPP Amazon data are uniform on two fixed intervals.

---


### 173. [Counterfactual Rollouts for Offline Contrastive Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2610.14953)

**<font color=#1a73e8>作者：</font>** Tingrui Huang, Ai Bo, Junzhe Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive reinforcement learning (CRL) learns goal-conditioned values by associating state--action pairs with the states subsequently reached, assuming that no unobserved variable jointly affects the recorded action and its outcome. When offline demonstrations come from a demonstrator with information hidden from the learner, this assumption fails and the critic absorbs spurious action--outcome associations. We formalize this setting with confounded Markov decision processes and introduce counterfactual transitions that separate what the data identify from what they do not; minimizing over all compatible transitions yields a worst-case occupancy that lower-bounds the true one. Causal Contrastive Reinforcement Learning (CauCRL) learns a pessimistic counterfactual transition from positive and negative offline demonstrations and trains the critic on counterfactual rollouts, substantially improving success rates over standard CRL on confounded goal-reaching tasks.

---


### 174. [CatPortrait: Taming Video Generative Models for Portrait Animation via In-context Conditioning](https://arxiv.org/abs/2610.14957)

**<font color=#1a73e8>作者：</font>** Ziqi Ni, Zhou Fang, Shijian Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video generative models have shown strong capability in synthesizing high-quality and temporally coherent videos. Yet, adapting them for controllable portrait animation remains nontrivial, as existing methods typically rely on architectural changes or extra conditioning modules, increasing complexity and reducing compatibility with pretrained models. We present CatPortrait, a simple and effective framework that enables controllable portrait animation via 3D face guidance as in-context conditioning. CatPortrait preserves the original video generation backbone and injects structured 3D facial guidance into the input space through spatial concatenation, allowing pretrained image-to-video models to animate portraits without sacrificing their pretrained priors. CatPortrait supports both video-driven and audio-driven portrait animation within a unified framework. Extensive experiments demonstrate that CatPortrait achieves competitive or superior results across both settings.

---


### 175. [AD-GS: Anatomical Density-guided 3D Gaussian Splatting for Sparse-View Dental CBCT Reconstruction](https://arxiv.org/abs/2610.14963)

**<font color=#1a73e8>作者：</font>** Zonglin Li, Kexian Xie, Feiran Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view Cone-Beam Computed Tomography (CBCT) reconstruction is essential for reducing radiation dose and scan effort, but remains underconstrained due to limited projection information. Recent 3D Gaussian Splatting (3DGS)-based CBCT reconstruction methods rely on gradient-driven densification, which becomes unstable under sparse acquisition and often leads to over-smoothed structures. We propose AD-GS, an Anatomical Density-guided 3D Gaussian Splatting framework that formulates Gaussian densification as an attenuation-aware Markov Chain Monte Carlo (MCMC) sampling process. By interpreting Gaussians as samples from an underlying anatomical attenuation distribution, AD-GS adaptively concentrates representation capacity in high-attenuation regions, enabling sharper structural boundaries under sparse projections. To further constrain reconstruction, we incorporate a semantic regularization based on zero-shot features from Segment Anything in Medical Images, enforcing multi-view consistency through semantic priors. Experiments on the ToothFairy3 dental CBCT dataset demonstrate that AD-GS achieves superior structural fidelity and boundary preservation compared with existing 3DGS-based approaches under sparse-view settings within the dental and maxillofacial setting. Code is available at this https URL.

---


### 176. [Cross-Material Magnetic Core Loss Prediction via Operating-Condition Matching and Partial Optimal Transport](https://arxiv.org/abs/2610.14964)

**<font color=#1a73e8>作者：</font>** Cong Yao, Yu Zheng, Zehao Hou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-material magnetic core loss prediction requires adapting to new material responses with limited measurements. Global feature alignment overlooks differences in source and target excitation coverage. This motivates selecting comparable samples and controlling each source measurement's alignment contribution. This paper proposes T-PCOT, a Transformer transfer method based on condition-supported partial optimal transport. Frequency, flux excursion, temperature, and waveform descriptors define a sparse graph of comparable operating conditions. A capacity-constrained transport plan distributes alignment across source measurements and leaves costly target mass unmatched. The plan is constructed from measured inputs before training and guides local waveform-feature consistency. An importance-weighted sampling scheme preserves both uniform source regression and the transport objective during minibatch optimization. Experiments on three material pairs and three target label budgets show that T-PCOT reduces mean relative error (MRE) and 95th-percentile error (P95) relative to Transformer-based multiple-kernel maximum mean discrepancy (T-MKMMD) in all nine comparisons. Macro MRE decreases from 12.60% to 9.65%, and macro P95 from 30.94% to 25.06%, corresponding to relative reductions of 23.41% and 19.01%. Controlled comparisons and ablations examine the roles of input processing, condition correspondence, and source capacity. The results demonstrate the predictive advantage of organizing cross-material alignment through operating-condition support over the compared global alignment method. The proposed method achieves state-of-the-art predictive performance in magnetic core loss transfer learning.

---


### 177. [HodgePhaseNet: Discrete Hodge Decomposition of Semantic Flows in Transformer Attention](https://arxiv.org/abs/2610.14971)

**<font color=#1a73e8>作者：</font>** Kiyotaka Kasubuchi, Kazuo Fukiya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> WavePhaseNet introduced frequency-resolved semantic representations, QuantumPhaseNet introduced gauge-covariant phase connections, and ModularPhaseNet made a finite cyclic phase channel and its cycle holonomy computable in an ordinary Transformer. These constructions are complementary, yet they do not by themselves separate an observed collection of pairwise relations into a globally consistent direction, circulation around local compositions, and circulation that persists around a larger unfilled cycle. HodgePhaseNet addresses this separation by representing semantic transitions as an antisymmetric real-valued 1-cochain on a finite oriented simplicial complex. With vertex-edge incidence matrix $B_1$ and edge-face incidence matrix $B_2$, every such field has a unique orthogonal decomposition $\Omega = B_1^T\Phi + B_2\Psi + H$, where $B_1H=0$ and $B_2^TH=0$. The three component fields are unique even when their potentials are not. We give explicit projectors, a sparse implementation, integrability and gauge results, a verified numerical example, and a redesigned attention interface. The attention bias is defined on allowed ordered query-key pairs, remains consistent under arbitrary choices of edge orientation, and preserves a decoder's causal information boundary by constructing its complex from the visible prefix. Gauge invariance of the attention output is conditional on using invariant or appropriately compensated features. A simple difference of vertex embeddings has no coexact or harmonic component; a genuine relation encoder is therefore indispensable. Local circulation is not automatically contradiction, and harmonic flow is not automatically missing knowledge. These interpretations and any reduction in factual error require controlled empirical evaluation. This paper presents a mathematical and architectural proposal, not external natural-language performance results.

---


### 178. [Fitting Every Hint Is Not Enough: Premature Floods in Recurrent Algorithmic Reasoners](https://arxiv.org/abs/2610.14982)

**<font color=#1a73e8>作者：</font>** Amin Najafgholizadeh, Mohsen Afsharchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent algorithmic reasoners are trained with per-step hints on small graphs and run for many more steps on large ones. On breadth-first search in SALSA-CLRS, we find that a reasoner can reproduce every training hint and still fail on deep graphs: after some exact steps, it declares nodes reached before the search gets there. We call this a premature flood and trace two routes to it. In our GRU processor with a degree input, the flood is carried in the hidden state and set off when that input is in the tail of the training distribution. Setting the input higher at inference brings the flood sooner, and none of the six flooding models counts steps. Without the input, summing the neighbors' states instead of averaging them also breaks the processor. In the benchmark's own GIN and PGN, trained with its code, some seeds instead flood from a fixed step, on sparse and dense graphs alike. Clamping the degree input or adding 200 dense training graphs removes every failure of the GRU processor. Detaching the state between steps avoids the flood in that processor (0 of 23 seeds, against 6 under full backpropagation) but not with sums or a residual update, and two published remedies leave floods. None of the benchmark's test sets is both deep and dense, but its deepest one shows the second route: on its Delaunay graphs at 1,600 nodes, one GIN seed floods from step 18. We therefore recommend auditing the range of every input and aggregate, which catches the first route, and testing on deep graphs, which catches both.

---


### 179. [Mixing Regularization for Average-Reward $Q$-Learning and $Q$-Planning](https://arxiv.org/abs/2610.14988)

**<font color=#1a73e8>作者：</font>** Julien Roger, Sam Bodmer, Jian Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The average-reward setting for reinforcement learning is challenging because its Bellman operator is known to contract in span only when the underlying Markov chain is mixing. Whereas existing work typically assumes a contraction property, e.g., through environment mixing, we consider the setting where we are given a reward-agnostic $m$-step mixing policy, and we control the contraction and exploration properties of the learned policy by regularizing toward the mixing policy. We provide finite-time analysis of $Q$-learning algorithms that can be instantiated with multiple choices of regularization, with guarantees measured with respect to the regularized fixed point. Our framework exposes novel regularizer-dependent objects that control contraction, exploration, and operator bias. In the one-step setting, our rates match the best known rates for $Q$-iteration and synchronous $Q$-learning, and for $m$-step mixing we derive new rates. We also study $Q$-planning variants, and show that planning acts as time-localized learning, where the planning horizon $H$ trades off the bias from the boundary value against the sample complexity. Finally, we present numerical studies validating the analysis: (i) knowledge of a strong mixing policy improves convergence and exploration, and its advantage increases with bottleneck severity and, (ii) our theory predicts the convergence and bias rankings of regularizers from the $\alpha$-divergence family.

---


### 180. [Characterizing the Separability Gap in Prior-Data Fitted Networks](https://arxiv.org/abs/2610.14989)

**<font color=#1a73e8>作者：</font>** Julius Kobialka, Manuel Hülskamp, Thomas Nagler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior-data fitted networks (PFNs) are transformers pretrained on simulated datasets to approximate Bayesian posterior predictive distributions. Standard PFN theory assumes a separable task prior, under which the feature distribution and the mechanism generating labels from features are independent. We show that common PFN priors are non-separable, even in simple settings. Consequently, standard pretraining targets a predictive distribution based on a task posterior updated using both the labeled context and the query features. We characterize its difference from the predictive based on the context posterior alone and show that this difference vanishes under posterior concentration. Under misspecification (i.e., when the true joint distribution lies outside the prior's support), however, prior non-separability can favor better feature fit at the expense of conditional label fit. We illustrate the consequences for feature attribution, Bayesian optimization, and martingale checks of Bayesian behavior. The same dependence also enables PFNs to learn from additional unlabeled observations. We demonstrate this with SemiTabICL, a PFN explicitly pretrained to use these observations, which improves accuracy over a matched supervised baseline. Our findings highlight the need for explicit rules on unlabeled data use in PFN evaluation and establish the dependence between feature and label distributions as a consequential prior design choice.

---


### 181. [Certify the Decision, Not Every Score: Exact Top-k Selection from Few Evaluations](https://arxiv.org/abs/2610.14996)

**<font color=#1a73e8>作者：</font>** Yuhe Sui, Yingzhi Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Choosing a few robust algorithms or schedules can require evaluating every candidate under many adverse scenarios, even though an agent only needs to identify the winners. A predictor may suggest those winners, but cannot rule out a surprise in an unevaluated scenario. We introduce Certified Adaptive Selection (CAS), which returns the exact top-$k$ set as soon as remaining uncertainty cannot change it. CAS keeps guaranteed lower and upper bounds on Expected Shortfall (ES), the average loss in the worst scenarios. Its stopping test compares the worst admissible selected candidate with the best admissible excluded one; for information-disjoint Cartesian intervals this one-cut test is necessary and sufficient. Prediction has a separate role: selecting the next outcome to evaluate, never authorizing the decision. For empirical ES with exact unit-cost queries, we compute in polynomial time the fewest evaluations that could have proved the realized decision in hindsight. Our prediction-guided agent CAS-PG is exact for every predictor, including adversarial ones. On two public algorithm-selection matrices, CAS-PG certifies the exact top three after 630 of 3150 and 981 of 2200 replayed queries, or $1.14$ and $1.18$ times that hindsight minimum. Without historical outcomes, its transcript-only variant requires $1.28$ and $1.37$ times the minimum, outperforming the tested non-predictive certified policies. Separately, a prediction-free CAS policy avoids $93.0\%$ of exact recourse solves in synthetic energy scheduling. One certificate thus supports several acquisition policies and separately proved risk/cost extensions: prediction changes the work, not the justified choice.

---


### 182. [On the Complexity Gap Between POMDPs and Multi-Environment POMDPs](https://arxiv.org/abs/2610.15010)

**<font color=#1a73e8>作者：</font>** Eline M. Bovy, Caleb Probine, Marnix Suilen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-environment POMDPs (ME-POMDPs) generalize POMDPs by encoding a finite set of possible environments, capturing model uncertainty. The finite-horizon robust reward maximization problem for a ME-POMDP asks for a policy that maximizes reward in the worst environment, and recent work has shown this problem to be $\mathsf{PSPACE}$-complete. We expand the complexity landscape of ME-POMDPs by identifying which subclasses retain this $\mathsf{PSPACE}$-completeness. In particular, we take subclasses of POMDPs that are tractable in the single-environment case, and investigate the computational complexity of these classes when extended to the multi-environment setting. We first prove the $\mathsf{NP}$-completeness of multi-environment blind MDPs and deterministic POMDPs using a certain closure-under-mixture condition. We then prove $\mathsf{PSPACE}$-completeness for a range of subclasses that do not satisfy that closure condition, yielding new complexity results for multi-observation POMDPs. Finally, we show existential theory of the reals ($\exists \mathbb{R}$)-completeness for numerous ME-POMDP problems under time-dependent Markovian policies or finite-state controllers that are $\mathsf{NP}$-complete for standard POMDPs. These results reveal a subtle relationship between POMDP and ME-POMDP complexity that depends heavily on the subclasses involved.

---


### 183. [Conformal Sequential Decision Making With Cost and Sublinear Policy Regret Guarantees](https://arxiv.org/abs/2610.15011)

**<font color=#1a73e8>作者：</font>** Jayadev Naram, Giuseppe Durisi, Matteo Zecchin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated decision makers, such as AI agents that control robots or network devices, must often satisfy hard cost constraints while maintaining competitive performance. In such settings, a cost measure, such as a safety violation rate, energy consumption, or a distortion level, must stay within a given budget in every episode of operation. Furthermore, a cumulative reward metric, accounting for per-step performance, must stay close to the reward of a meaningful reference policy. We formulate this setup as an episodic sequential decision problem in which the state sequence is arbitrary, and the reward and cost may depend on past actions within the same episode. We propose the online conformal episodic agent (OCEA), a policy that selects one candidate action per episode using a regret-controlled algorithm, and switches to a zero-cost action when the remaining budget cannot absorb the maximum cost of one more round. We prove that OCEA satisfies per-episode cost constraints for every state sequence and for every realization of its internal randomness, while achieving a sublinear expected policy regret with respect to the best action sequence in hindsight from a comparator class satisfying the same per-episode cost constraints. We apply OCEA to risk-averse control and online compression with distortion guarantees.

---


### 184. [CowCare: A Unified Visual Framework for Viewpoint-Robust Cattle Tracking and Spatiotemporal Heat-Stress Analysis](https://arxiv.org/abs/2610.15012)

**<font color=#1a73e8>作者：</font>** Xin Liu, Weiran Li, Minghao Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable individual monitoring is essential for dairy cattle welfare and early heat stress detection in Precision Livestock Farming (PLF). However, translating raw multi-camera videos into automated diagnostics remains challenging due to disconnected tracking and recognition pipelines and complex physical environments. Dense mutual occlusions and cross-camera viewpoint variations fragment identities, while environmental noise, including camera vibrations, and limited agricultural data obscure subtle heat stress cues such as rapid breathing and flank undulations. To bridge low-level visual features and high-level behavioral diagnostics, we propose CowCare, a unified framework combining viewpoint-robust tracking with spatiotemporal heat stress recognition. Its tracking module, CowTrack, maintains cross-camera identity consistency through a View-Decoupled Aggregation Network (VDA-Net). Instead of relying on static global representations, VDA-Net aggregates localized textures under heavy occlusion and uses a Viewpoint Decoupling Transformer (VDT) to suppress transient viewpoint variations. CowTrack further incorporates a causal online self-supervision mechanism for continuous adaptation to dynamic farm scenes. The resulting tracklets are subsequently processed by TSDF-Net, a fine-grained video understanding network. Its Temporal Stabilization and Aggregation Module (TSAM) suppresses high-frequency jitter, while a Diffusion Semantic Prior (DSP) uses frozen pre-trained diffusion semantics to enhance subtle behavioral signals and mitigate overfitting. Extensive evaluations on two real-world farm benchmarks demonstrate the framework's effectiveness: CowTrack achieves 83.48% HOTA and 87.72% IDF1 for global multi-object tracking on MVCow, and TSDF-Net achieves 87.72% Top-1 accuracy on HSCow. These results establish CowCare as a robust end-to-end framework for automated livestock health monitoring.

---


### 185. [Algorithmic Fairness Over Time: Advances & Prospects](https://arxiv.org/abs/2610.15015)

**<font color=#1a73e8>作者：</font>** Miriam Rateike  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the presence of feedback loops, algorithmic decisions at one time step can influence observed data in subsequent steps, potentially introducing selection bias or shifts in data distribution. Research has demonstrated that ignoring these effects can lead to unfairness, which may worsen over time as the model remains deployed within society. This raises important questions of how to measure and ensure fairness of algorithmic decision-making models over time. In this short paper, we present a taxonomy that distinguishes between different types of static and temporal fairness notions in recent advancements. We then suggest prospects for future research by identifying common implicit temporal assumptions, open questions to enhance our temporal understanding of fairness, and other open challenges.

---


### 186. [PATTERN Can Be Solved from Memory: Generator-Aware Baselines for Synthetic Node Classification](https://arxiv.org/abs/2610.15020)

**<font color=#1a73e8>作者：</font>** Amin Najafgholizadeh, Mohsen Afsharchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> PATTERN, a synthetic node-classification benchmark still used to rank graph networks, plants a random subgraph in a random host graph and asks which nodes belong to it. Its generator draws 100 patterns once and plants the same ones in every split, so each test graph carries a pattern that also appears in 100 training graphs. A matcher that reads these patterns off the training labels and looks them up in each test graph reaches 99.2 class-weighted accuracy with no trained parameters, against 89.8 for the best published model. Inference under the generator without the patterns reaches 86.8. Two published models, CKGConv and GRIT, score lower on patterns they have not seen: on new graphs with fresh patterns both fall below this pattern-blind predictor, and withholding patterns from CKGConv's training lowers its accuracy on the test graphs that carry them. Training CKGConv with a new pattern in every graph raises its accuracy on fresh patterns by about 2 points, to the level of the pattern-blind predictor, at some cost on the reused patterns. The same kind of inference under the generator matches the best published result on CLUSTER and, without any training, scores above every published result we found on Minesweeper's released board. We recommend that synthetic benchmarks report scores on fresh templates beside reused ones, publish baselines built from their generators, and state how their metric is weighted and pooled.

---


### 187. [EnRoute: Iterative Design and Evaluation of a Mobile App for Lower-Carbon Fashion and Transportation Choices](https://arxiv.org/abs/2610.15026)

**<font color=#1a73e8>作者：</font>** Angela Busheska  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> EnRoute is an iOS application designed to support more sustainable everyday choices in transportation and fast fashion consumption. We describe three design iterations and the user research and field evaluations that shaped each one. Interviews with 15 people from 12 countries informed Version I, which combined errand route planning with basic fashion guidance. A survey of 1,200 people in five countries found much stronger interest in sustainable shopping (78%) than in switching to lower-carbon transport (46%); respondents most often named limited public transport as the main barrier to lower-carbon travel. We therefore narrowed the focus to fashion. Version II added item-level garment scanning with a manual-entry fallback, a Sustainability Coefficient that rates items, and recommendations of more sustainable alternatives; in a two-week evaluation with 3,021 participants in eight countries, participants randomly assigned to receive a short tutorial and educational prompts viewed more recommended alternatives and reported larger gains in purchase intent than those without it. Version III shifted from "buy better" to "buy less," adding a wardrobe inventory, outfit matching, and a "Real Price" that combines cost per wear with estimated environmental and social costs. In a four-week pre/post pilot with 500 participants, self-reported monthly garment purchases fell from 2.9 to 1.9. We report descriptive results, discuss the substantial limitations of these uncontrolled and self-reported measures, and outline what the iterations suggest about designing for sustainable consumption.

---


### 188. [Appearance Compensation in Volume Rendering](https://arxiv.org/abs/2610.15030)

**<font color=#1a73e8>作者：</font>** Jianghong Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a volume that reproduces every external RGB view still have an incorrect density? We study this question in emission-absorption rendering with an independently parameterized, physically bounded effective source. Appearance compensates a density change by replacing the radiance that it removes from the rest of each ray. We characterize the surviving density information with a shared spatial appearance field. Our first result is an optimal density-only gain after finite-degree spherical-harmonic source refitting. A coupled tensor gauge and physical localized packets identify the sharp limiting nonlinear inverse coefficient as its reciprocal. Our second result realizes positive gain at every fixed finite degree for a residual set of isotropic spatial sources at one fixed density. At the same references, growing angular capacity hides a fixed nonzero density error while retaining physicality and any prescribed finite set of smoothness bounds. Local identifiability and the absence of a capacity-uniform recovery modulus therefore coexist. Our third result constructs an exact physical SH2 ambiguity: central density doubles and relative density $L^2$ error exceeds $14.52\%$, yet every external RGB ray is unchanged. We connect these continuum results to shared finite representations, continuous pixel measurements and density-sensitive acquisition. Complete-class certificates separate SH0, SH1 and SH2 fits at one learned density. Finite-camera results expose the distinct role of spatial capacity, and transmission measurements separate otherwise identical RGB fields. Controlled training tests and captured-smoke profiles supply mechanism evidence with explicit observation scopes. The results show why rendering accuracy alone cannot certify density: recovery also depends on appearance capacity, spatial resolution and measurement design.

---


### 189. [InCLAD: A Continual Learning Benchmark for Industrial Visual Anomaly Detection](https://arxiv.org/abs/2610.15032)

**<font color=#1a73e8>作者：</font>** Łukasz Marcjan, Dorota Wilk-Kołodziejczyk, Roberto Corizzo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection benchmarks have advanced rapidly, yet they remain largely static and therefore underrepresent deployment settings in which inspection systems must be extended from one industrial component to another over time. In our setting, continual industrial anomaly detection is framed as a task-incremental problem: each component defines a task, while the learning objective remains semi-supervised. The goal extends beyond conventional anomaly detection, since models should preserve their performance on all components as they are sequentially exposed to new components. This framing is especially relevant because many existing industrial pipelines either assume fully supervised defect labels or study only isolated datasets, leaving open the question of how semi-supervised anomaly detectors behave across a sequence of heterogeneous components. We address this gap by organizing the benchmark as a sequence of related component-level tasks and by defining multiple scenarios, including random, easy-to-hard, and hard-to-easy. In addition to single-dataset continual scenarios, we propose challenging scenarios spanning across multiple datasets. We further evaluate continual performance from two complementary perspectives: image-level anomaly detection and pixel-level anomaly localization. By recasting industrial anomaly detection as a continual benchmark rather than a static train/test problem, our work establishes a concrete path toward studying knowledge retention, adaptation, and generalization in evolving industrial environments.

---


### 190. [Belief Embedding Tree Search](https://arxiv.org/abs/2610.15046)

**<font color=#1a73e8>作者：</font>** Christopher Solinas, Radovan Haluška, Martin Schmid 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Beliefs in a Partially Observable Markov Decision Process (POMDP) are posterior distributions over the hidden state given the agent's history of actions and observations. They summarize everything the history says about the state, so planning in a POMDP is planning in a Markov decision process (MDP) over beliefs. Belief MDPs have continuous state spaces even for finite POMDPs, and exact planning in them is intractable in general. Planners must therefore approximate beliefs and estimate values. Monte Carlo planners do both inside a search tree, with an approximate belief at every node and a value estimate at every leaf. Approximations usually consist of sets of sampled states, with leaf values coming from rollouts, hand-designed bounds, or learned networks. Policies and values computed from these approximations are limited by their quality, and prior methods with learned networks rely on hand-chosen summaries of the sampled states. A belief representation should be computable from the parent node's representation through the POMDP's dynamics, let the search sample from it, and be learned so that it provides the information that policies and value functions need. We present Belief Embedding Tree Search (BETS), a Monte Carlo planner that meets these requirements by representing each node's belief with a generative distribution embedding (GDE) while updating it through the POMDP dynamics. BETS trains its belief model alongside its policy and value networks through experience, with the realized hidden state of the POMDP as the belief model's training target. We evaluate BETS on six configurations of RockSample, LightDark, and PocMan against BetaZero and three planners without learned components. BETS is competitive or leading on all six, while every baseline falls far behind on at least one. Where beliefs are highest-dimensional, it outperforms them by a large margin, even without search.

---


### 191. [Use Of Convolutional Neural Networks In Detection Of Branch Dieback Disease In Pequi Trees](https://arxiv.org/abs/2610.15049)

**<font color=#1a73e8>作者：</font>** Ronilson Rodrigues Pinho, Elua Ramos Coutinho, Nilza de Lima Pereira Sales 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study aims to evaluate and compare convolutional neural network (CNN) architectures, specifically AlexNet, Inception, LeNet, VGG16, and MobileNet, for diagnosing branch dieback (seca-dos-ponteiros) in pequi trees (Caryocar brasiliense). This disease represents a severe threat to tree development and fruit yield, causing substantial economic and ecological losses. The methodology implements computer vision techniques using Python libraries, including Scikit-learn, NumPy, TensorFlow, and Matplotlib, to process and evaluate visual data. The CNN models analyze images of leaves, branches, and flower spikes to detect pathological patterns, such as alterations in texture and coloration. Ultimately, this comparative analysis identifies the most effective architecture for accurately distinguishing healthy plants from diseased ones.

---


### 192. [Deep Learning-based Semantic Segmentation of Dental Radiographs: Comparative Evaluation of PSPNet, DeepLabv3, UNet, and UNet++](https://arxiv.org/abs/2610.15061)

**<font color=#1a73e8>作者：</font>** Malithi Nawarathne, Nadeesha Herath Mudiyanselage Lihini Sangeetha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and efficient analysis of dental radiographs has become increasingly important for disease diagnosis and clinical decision making. In particular, dental radiographs segmentation plays a critical role as it is challenging due to several reasons, such as low contrast, noise in the images, variations in the image quality, etc. Previous studies have primarily addressed these challenges using convolutional neural networks (CNN)-based models. However, direct comparison of these segmentation models is still challenging due to the variations among the experimental settings. Therefore, we mainly compared four segmentation models, including Pyramid Scene Parsing Network (PSPNet), DeepLabV3, UNet, and UNet++, through a fair, controlled experimentation setting under varying conditions such as image sizes and batch sizes. For this, we used 1269 dental radiography images, and prior to training, we implemented a series of preprocessing techniques. To assess the models, we used several metrics, including Dice coefficient (DICE), Intersection over Union (IoU), accuracy, precision, training and validation losses. According to our results, UNet++ demonstrated the highest IoU score of 0.6719, and a DICE value of 0.7869, showing superior results in terms of segmentation, specifically when configured with an image size of 300x300 and a batch size of 16. In addition, we also explored the effect of image resolutions and batch sizes on model performance and accuracy under different architectures. Therefore, this study provides insights into the strengths of different segmentation models and the potential of deep learning-based semantic segmentation methods for improving automated dental radiograph analysis.

---


### 193. [Exposing AI Inference as a Telco Network API over the 5G User Plane](https://arxiv.org/abs/2610.15062)

**<font color=#1a73e8>作者：</font>** Rodrigo Moreira, Larissa Ferreira Rodrigues Moreira, Joberto S. B. Martins 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supporting edge Artificial Intelligence (AI) inference as a network service is challenging because current mobile systems can transport tensors but do not expose or understand the inference context that gives those tensors operational meaning. Prior studies have addressed this gap through dynamic partitioning, collaborative inference, and split pipelines; however, these solutions remain application-bound, network-blind, or context-free. This work proposes Inference on Demand (IoD), an inference-on-demand abstraction that exposes split inference through a CAMARA-like Application Program Interface (API) and carries a split-aware tensor context in-band across the 5G user plane path. We evaluate the IoD on a programmable user plane function (UPF)-based testbed using a partitionable visual AI workload, showing that adaptive split selection can operate as a network-facing service while avoiding the rigid cost profile of static configurations. Including our findings, split inference becomes more than offloading when the service intent, runtime partitioning, and tensor transport are made visible to the mobile data plane. This opens a path toward network-native AI services, in which programmable telco infrastructure coordinates computation, context, and connectivity for user-facing applications.

---


### 194. [Global Disaster Risk Assessment Using World Risk Index Data: A Geospatial and Visual Analytics Approach](https://arxiv.org/abs/2610.15064)

**<font color=#1a73e8>作者：</font>** Malithi Nawarathne, Nadeesha Herath Mudiyanselage, Lihini Sangeetha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The world has seen several threats that include resource depletion, food security, poverty and inequality, difficulties associated with urbanization, migration, and environmental effects. The World Risk Index (WRI) is a metric that is used to measure the susceptibility of nations against natural disasters and related risks that is reported by the Humanitarian Data Exchange. The WRI is comprised of factors such as susceptibility, vulnerability to natural hazards, and coping mechanisms. The WRI index has allowed to recognize regions in advance in order to face threats and situations beforehand. This study was conducted by analyzing the data that was related to years from 2000 to 2025 using data visualization techniques. Python related libraries of Matplotlib, Seaborn, and Geopandas were used due to their efficiency and usability in analyzing WRI data. As per the analysis, it was identified that countries of Philippines, Mexico, Indonesia, and India were recorded with high WRI index values that showed these nations should be prepared for natural disasters and situations. Hence, this study has provided insights using data visualization techniques in understanding natural disasters and threats so that necessary measures can be taken

---


### 195. [MotionAnimator: Semantic-to-Motion Reasoning for Animating Part-Structured 3D Assets in XR](https://arxiv.org/abs/2610.15074)

**<font color=#1a73e8>作者：</font>** Jianan Jiang, Bin Li  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> 3D digital assets are increasingly used in education, simulation, design, and immersive content creation, yet most remain behaviorally inert: they provide geometry and component structure but lack the semantic annotations, motion constraints, and executable behaviors needed to function as dynamic objects in Extended Reality (XR). Animating such assets therefore still requires manual rigging, object-specific templates, or substantial programming expertise. We introduce MotionAnimator, an intent-driven, part-aware XR animation authoring system that transforms semantically unlabeled, part-structured 3D assets into executable animations from natural-language instructions. Rather than generating code directly from text, MotionAnimator externalizes object understanding and motion reasoning into explicit semantic and motion representations. It grounds object identity, semantic parts, and functional directions, constructs a structured plan that coordinates object- and part-level motion, and translates the plan into executable Unity behavior. On a benchmark of 90 prompts across 30 objects, MotionAnimator demonstrated reliable semantic grounding and coordinated animation generation across diverse objects and animation intents. An exploratory user study further provided insights into users' experiences with MotionAnimator and highlighted its potential for part-aware XR animation authoring. These findings demonstrate how explicit semantic and motion representations can bridge high-level user intent and executable behavior, enabling existing part-structured assets to support coordinated XR animations beyond object-level transformations and predefined behaviors.

---


### 196. [BrainAid: Efficient Brain Tumor Detection Using Lightweight CNNs and Explainable AI for Resource-Constrained Environments](https://arxiv.org/abs/2610.15077)

**<font color=#1a73e8>作者：</font>** Sai Sriram Gonthina, Ross Gore, Bikash Chandra Singh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A brain tumor is an unusual growth of cells in the brain that can be cancerous or not, affecting normal brain function and causing serious risk to health. Existing solutions for brain tumor classification, such as expert manual evaluations of magnetic resonance imaging (MRI) scans, are generally inconsistent as different professionals have different criteria and can be resource-intensive, leading to delayed diagnoses. Additionally, while deep learning models have demonstrated potential, they typically require significant computational resources, motivating the need for more efficient and accessible diagnostic tools that can be deployed in real-time healthcare settings. To address these limitations, this study presents BrainAid, which makes efficient use of Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) for effective classification of four-class classification of glioma, meningioma, pituitary tumor, and no-tumor MRI scans, outperforming all the standard models such as VGG16, Inception-V3, ResNet-50 and so, while integrating Explainable AI (XAI) to improve interpretability. The BrainAid is trained to classify tumors with a high precision of 98%, achieving an F1 score of 98% and an accuracy of 98% using publicly available dataset. The model is deployed on a Raspberry Pi, demonstrating efficiency in low-resource environments. This system shows the feasibility of real-time, edge-based tumor classification, providing quick diagnostic support for medical professionals and enhancing patient care in resource-limited healthcare facilities and underserved areas.

---


### 197. [On the Theoretical Limits of Learning Unconstrained Interatomic Potentials](https://arxiv.org/abs/2610.15078)

**<font color=#1a73e8>作者：</font>** Prajwal Ananth, Shuwen Yue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learned interatomic potentials (MLIPs) accelerate molecular dynamics (MD) simulations by learning the energies and forces that govern atomic motion. Recent work has shown that relaxing physical inductive biases can improve computational efficiency and predictive accuracy, raising the question of whether energy-and-force matching alone is sufficient to ensure accurate sampling. We show that, for unconstrained hypothesis classes, the relationship between prediction error and sampling accuracy is exponentially ill-conditioned in dimension. In particular, prediction errors that decay exponentially with dimension can coexist with nearly maximal total variation distance between the learned and target distributions. We identify two failure mechanisms. The first is kinetic trapping, where relaxation to an accurate learned equilibrium requires exponentially long times, even when simulations are initialized from training configurations at which energies and forces are matched exactly. The second is equilibrium mismatch, where the learned stationary distribution itself remains far from the target. Under explicit assumptions, we show that equilibrium mismatch can persist even in local, symmetry-preserving models, where small per-atom errors coexist with a distributional discrepancy that approaches its maximum as system size increases. Finally, we establish global energy-control conditions that guarantee equilibrium accuracy and identify additional conditions required for rapid relaxation.

---


### 198. [Region Aware Squeeze-and-Excitation Networks for Image Segmentation](https://arxiv.org/abs/2610.15079)

**<font color=#1a73e8>作者：</font>** Jack Roberts, Praneeth Tummala, Kavi Sarna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Squeeze-and-Excitation (SE) modules improve convolutional networks by modeling channel-wise dependencies, but global average pooling collapses spatial structure into a single per-channel descriptor, limiting their effectiveness for dense prediction tasks such as image segmentation. We generalize SE by replacing global pooling with spatially guided pooling, enabling region-aware channel recalibration through four modules with complementary cost profiles. BASE formalizes Tiled Squeeze-and-Excite using a regular grid; SPASE pools over SLIC superpixels for image-adaptive regions; MAPSE obtains regions from semantic maps produced by a frozen, general-purpose network; and PLEASE learns soft region assignments end-to-end through a lightweight assignment network. Each channel receives one gate per region, so attention at each pixel reflects its region membership, bridging channel and spatial attention. PLEASE also produces its soft assignments as a byproduct of the forward pass, providing structured spatial interpretability without post-hoc analysis. The modules offer complementary computational tradeoffs: some add essentially no parameters, while others add no measurable latency. Across binary segmentation on CUB, DUTS, and ECSSD, semantic segmentation on PASCAL VOC 2012 and ADE20K, and classification on mini-ImageNet, our modules outperform SE and related spatial-channel attention variants on most benchmarks, achieving the majority of best results.

---


### 199. [Self-Evolving Visual Agent via Margin Reward](https://arxiv.org/abs/2610.15084)

**<font color=#1a73e8>作者：</font>** Wenxi Yang, Yuzhong Zhao, Baochang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual agents that interleave reasoning with tool invocation have posed a promising direction for multimodal tasks. However, learning effective tool invocation usually relies on curated question-answer pairs or expert demonstrations at scale, which are expensive to acquire. In this study, we propose Marvo, a simple-yet-effective self-evolution approach that enables learning tool invocation from unlabeled images. Marvo consists of two agents: (1) a challenger that generates question-answer pairs from unlabeled images, and (2) a solver that learns tool invocation by solving questions through reinforcement learning. To encourage effective tool invocation, a good training question should be difficult enough to warrant tool use, yet remain within the solver's capabilities. To this end, we introduce a margin reward to the challenger, defined as solver's performance difference with and without access to tools. With the margin reward, we create an adaptive curriculum that encourages the solver to learn effective tool invocation. Across benchmarks covering agentic reasoning, visual search, mathematical, and general real-world reasoning, Marvo improves average accuracy by up to 7.1\% --- demonstrating margin reward as a preferred way to scale question complexity without human supervision.

---


### 200. [VLCQ: Post-training quantization for deep neural networks using variable length coding](https://arxiv.org/abs/2610.15092)

**<font color=#1a73e8>作者：</font>** Reem Abdel-Salam, Ahmed H. Abdel-Gawad, Amr G. Wassal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantization plays a crucial role in efficiently deploying deep learning models on resource-constrained devices. Post-training quantization does not require access to the original dataset or retraining the full model. Current methods that achieve high performance close to baseline results typically require INT8 fixed-point integers. However, achieving higher model compression with lower bit-widths often leads to significant performance degradation. In this paper, we propose VLCQ, a post-training quantization method that relaxes the fixed-point encoding constraint, enabling more flexible exploration of quantization techniques through variable-length encoding. This approach achieves competitive or improved performance while reducing bit-widths, without requiring access to training data or model fine-tuning. Extensive experiments on image classification, segmentation, and object detection demonstrate that VLCQ improves model compression and accuracy compared with state-of-the-art post-training quantization approaches. For per-channel quantization, VLCQ surpasses FP32 accuracy and Piece-Wise Linear Quantization (PWLQ) on most evaluated models, achieving up to 6x compression compared with FP32 and up to 1.7x compared with PWLQ. When prioritizing compression with limited accuracy loss, VLCQ achieves up to 12.25x compression compared with FP32 with less than 4% performance degradation. For per-tensor quantization, VLCQ is competitive with Data-Free Quantization (DFQ), while providing greater flexibility to achieve lower bit rates across different tasks and models.

---


> [!TIP]
> 当前位于：**151-200**（第 4/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
