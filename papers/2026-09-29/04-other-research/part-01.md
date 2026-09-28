# 📦 其他研究 | 2026年09月29日

> 本类共 **225** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-225](./part-05.md)

---

### 1. [When the Preconditioning Exponent Turns Negative: Learning-Rate Coupling and Cross-Environment Generalization](https://arxiv.org/abs/2609.30271)

**<font color=#1a73e8>作者：</font>** Gongyue Zhang, Honghai Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive optimizers are commonly parameterized by a fixed power of the second-moment estimate. Existing partially adaptive methods study exponents between momentum-like updates and the standard Adam square root, while the interaction between this exponent and the global learning rate is less understood. We perform a controlled cross-environment study using a paired four-environment classification problem with stable sparse features, environment-dependent spurious sparse features, dense features, and high-dimensional noise. Across \NumRuns{} source-training runs covering 21 preconditioning exponents $p\in[-0.5,0.5]$ and five learning rates $\eta\in[10^{-4},10^{-2}]$, we find that the exponent maximizing cross-environment accuracy decreases almost linearly with $\log_{10}\eta$. The fitted slopes range from $-0.270$ to $-0.300$, with $R^2$ between $0.972$ and $0.996$. At $\eta=10^{-2}$, source-validation selection still prefers positive exponents in all four environments, whereas cross-environment and worst-environment criteria prefer negative exponents. Checkpoint decomposition shows that lower $p$ reduces the learned spurious-to-stable and noise-to-stable weight ratios; under reversed correlation, it also reduces the magnitude of the harmful spurious margin. Negative $p$ is therefore not a universally optimal setting. It is a high-step-size allocation regime produced by the joint action of learning rate and preconditioning. The study also exposes a model-selection conflict: source-domain validation systematically selects a different preconditioning regime from the one that maximizes robustness to environmental change. The results are a single-seed, finite-budget mechanism study rather than a broad benchmark claim.

---


### 2. [ENAS: An Efficient Hardware-Aware Neural Architecture Search Framework for TinyML on Resource-Constrained Microcontrollers](https://arxiv.org/abs/2609.30272)

**<font color=#1a73e8>作者：</font>** Mohd Moin Khan, Naman Srivastava, Pandarasamy Arjunan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present \textbf{ENAS}, a hardware-aware Neural Architecture Search (NAS) framework that combines a static feasibility check, a cell-based search space supporting standard, depthwise-separable, and bottleneck blocks with optional skip connections, and a three-stage hybrid search strategy (random $\rightarrow$ top-$K$ $\rightarrow$ mutation) with persistent cross-run caching. Unlike many existing NAS frameworks that rely on GPU acceleration, ENAS is designed to operate efficiently without requiring GPUs, making it suitable for resource-constrained development environments. We evaluate ENAS on two TinyML benchmarks, Visual Wake Words and Melanoma Cancer, across eight microcontrollers with memory footprints ranging from 20\,KB to 1\,MB SRAM and nine input image resolutions. Our experimental results show that ENAS achieves mean search-time speedups of $2.41{\times}$ and $1.70{\times}$ on the Visual Wake Words and Melanoma Cancer datasets, respectively, while maintaining competitive test accuracy compared with the recent NanoNAS framework. A measured resource analysis further shows that ENAS-selected models use substantially lower peak activation RAM, the binding constraint for microcontroller deployment at matched accuracy. Additionally, ENAS achieves $79.4\%$ test accuracy on an STM32H743-based microcontroller, outperforming the greedy CPU-only baseline by $2.6$ percentage points. We release the ENAS framework as open-source at: this https URL

---


### 3. [Offline Policy Evaluation as a decision support tool for designing Adaptive Experiments](https://arxiv.org/abs/2609.30273)

**<font color=#1a73e8>作者：</font>** João Victor Ferreira Alves, Eduardo Rocha Laurentino, Gustavo de Oliveira Kanno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate how historical data from fixed randomized experiments (A/B tests) can be used to inform the deployment of adaptive experiments based on contextual bandits. Given data collected under a static allocation, our goal is to assess which adaptive policies, if any, would have outperformed the original design and under what conditions. To this end, we combine off-policy evaluation (OPE) with a controlled warm-start simulation. From logged A/B test data exhibiting heterogeneous treatment effects, we estimate nuisance components and use doubly robust estimators to rank a portfolio of pre-specified adaptive and non-adaptive policies. When ground truth is available, we then deploy the same offline-trained policies in a simulator that reuses the exact data-generating reward probabilities, providing a safe, ground-truth-anchored environment to study the offline-to-online transition under warm starting. Using synthetic randomized controlled trials with known heterogeneity structures and an oracle policy, our results indicate that adaptive, context-aware policies improve upon fixed allocations when meaningful heterogeneity is present, while providing little benefit in its absence. We reinforce our findings on standard open benchmarks (Hillstrom, Criteo Uplift, and LaLonde), reinterpreted through a policy-value and regret perspective. Overall, our results provide a practical methodology for deciding when adaptive experimentation is worth deploying and how to select among competing adaptive policies using existing A/B test data.

---


### 4. [Why Clipping Matters in AdaGrad? Toward a High-Probability Theory under Generalized Smoothness](https://arxiv.org/abs/2609.30276)

**<font color=#1a73e8>作者：</font>** Alokendu Mazumder, Ayaan Mohd, Harshit Rawat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We analyze the original same-step coordinate-wise AdaGrad under generalized smoothness and heavy-tailed noise with bounded variance. In this setting, local curvature may grow sub-quadratically with the gradient norm, and stochastic gradients are assumed to have only bounded conditional second moments. We show that unclipped AdaGrad can become \emph{anisotropically miscalibrated}: under heavy-tailed noise, the adaptive denominator can learn the geometry of rare noise shocks rather than the local curvature of the objective, leading to a persistent directional distortion that blocks finite-horizon Euclidean progress. We then prove that clipping repairs this failure mode. Our main result is a finite-horizon high-probability guarantee for the original non-lagged AdaGrad update, yielding $\frac1T\sum_{t=0}^{T-1}\|\nabla f(x_t)\|^2=\mathcal{O}\left(\frac{d\big(\sqrt{\log T} + \log \frac{1}{\delta}\big)}{\sqrt{T}}\right),$ and hence $\widetilde{\mathcal O}(\varepsilon^{-2})$ complexity. This shows that, for AdaGrad under heavy-tailed noise, clipping is a structural stabilizer of the adaptive geometry rather than merely a robustness heuristic.

---


### 5. [Fixed Points Without Fixed Diffusion: Implicit Neural Sheaves for Convergent Test-Time Computation](https://arxiv.org/abs/2609.30277)

**<font color=#1a73e8>作者：</font>** Rémi Bourgerie, Šarūnas Girdzijauskas, Viktoria Fodor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Implicit Graph Neural Networks (IGNNs) define node representations as fixed points of message-passing operators, enabling effectively infinite-depth propagation, iteration-independent parameterization, and flexible test-time computation. Yet these benefits depend on the equilibrium being unique and attainable by fixed-point iteration. Existing constructions often impose constraints on recurrent updates to obtain these guarantees, limiting the transformations available at equilibrium. This raises a central question: can IGNNs gain expressiveness through richer, edge-dependent transformations while retaining the inherent strengths of their equilibrium formulation? We introduce SheafDEQ, a subhomogeneous deep-equilibrium architecture with adaptive neural-sheaf propagation. Its learned, matrix-valued sheaf restriction maps can align, mix, or reverse neighbouring representations. Under mild regularity conditions, we prove that SheafDEQ admits a unique equilibrium reached globally by fixed-point iteration from any positive initialization. Contractivity further guarantees convergence under bounded communication staleness. We evaluate SheafDEQ on distributed-inference tasks requiring repeated nonlocal aggregation and on community detection whose rewiring increasingly favours cross-community interactions. SheafDEQ improves over fixed-propagation implicit baselines on Sums, MNIST Terrain, and Coordinates, and on community detection as connectivity becomes increasingly heterophilic. Continued-iteration diagnostics show decreasing residuals and low prediction sensitivity after 100 iterations for initialization scales from $0.001$ to $10$, while delayed-update experiments show low sensitivity to bounded communication staleness.

---


### 6. [Neural Ideals and Neural Codes: An Algebraic Framework for Neural Network Classification and Feature Interpretation](https://arxiv.org/abs/2609.30279)

**<font color=#1a73e8>作者：</font>** Venkata Subbaiah Yerrapati, Rahul Dixit, Ajay Kumar Shukla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the features captured by the hidden layers of neural networks is a fundamental challenge in machine learning, despite their widespread success across various classification problems. In this work, we propose an algebraic framework for examining neural networks that model classification problems. Certain results, such as the correspondence between the neural network and neural ideals, algorithms for computing the neural ideals, and a stabilization theorem that enables approximation of the neural ideals, are first established. As an application to the framework, we present algorithms to identify and interpret the features captured by each hidden-layer neuron. Along with these theoretical developments, the practical performance has been demonstrated on the MNIST digit dataset, and the results highlight the pivotal role of neural ideals as a mathematical and computational tool for analyzing the features captured by neural networks. Further, we develop an interactive software that builds on the presented framework to visualize the features captured by each neuron. This tool is available at this https URL

---


### 7. [Seasonal and Quantum-inspired Models for Neutron Monitor Time Series Forecasting](https://arxiv.org/abs/2609.30281)

**<font color=#1a73e8>作者：</font>** Krishna Bhatia, Shalini Devendrababu, Srinjoy Ganguly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a focused and reproducible study of multi-horizon forecasting on the Lomnicky Stit neutron monitor (LMKS) time series. Our evaluation suite covers simple seasonal baselines, modern deep sequence models, and functional and quantum-inspired architectures, including Seasonal Naive, Long Short-Term Memory (LSTM), Temporal Convolutional Network (TCN), N-BEATS, Kolmogorov-Arnold Networks (KAN), and two quantum-inspired variants, QiLSTM and QiKAN. We describe the dataset characteristics, diagnostic analysis, preprocessing pipeline, and training procedures, and report aggregate point-forecast performance using mean absolute error (MAE) and root mean squared error (RMSE) for all evaluated models. Our quick-run results indicate that the quantum-inspired KAN variant, QiKAN, achieves the lowest aggregate forecasting error among the evaluated configurations, while the simple Seasonal Naive baseline remains remarkably competitive. These results suggest that, for highly periodic scientific monitoring time series, models incorporating strong seasonal or low-dimensional functional priors can match or outperform substantially more complex sequence architectures. The findings motivate further investigation of parsimonious and decomposable function approximators for forecasting periodic scientific signals.

---


### 8. [When Does Advection-Aware Graph Nowcasting Help? A Controlled Study of Distributed Solar Ramp Forecasting with a Self-Supervised Cloud-Motion Estimator](https://arxiv.org/abs/2609.30286)

**<font color=#1a73e8>作者：</font>** Phillip Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short-term forecasting of cloud-induced power ramps across a network of distributed photovoltaic (PV) or irradiance sensors is a recognised pain point for grid operators. A natural idea is to make the graph neural network (GNN) advection-aware: connect each site to the sites upwind of it, with edge time-lags set by the cloud-motion vector (CMV), so that a ramp is propagated forward before it physically arrives. Using a controlled synthetic testbed with a known wind field, we show that (i) with a realistic cross-correlation CMV estimate, an explicit advection graph does not beat a plain static or learned-adjacency spatiotemporal GNN; (ii) roughly half of the benefit available from a perfect CMV comes simply from providing an accurate motion vector as an input feature, not from graph structure; and (iii) advection helps only when the advective displacement over the forecast horizon, v*H, fits inside the sensor network. Motivated by (ii), we introduce a small self-supervised cloud-motion estimator -- a position-aware encoder trained only on a multi-lag optical-flow reconstruction objective with an annealed kernel -- that recovers the true wind vector to 2-4 degrees median angular error, 2-4x better than the classical cross-correlation method across every wind regime. Freezing this estimator and feeding its vector to the forecaster closes about 60% of the oracle-CMV RMSE gap at moderate wind (8-15% RMSE reduction over no advection), with no external wind data. We also report a negative result for a spatially-coherent probabilistic head. All claims are established on a single synthetic simulator; we discuss why real-network validation is the necessary next step and outline it.

---


### 9. [A Mechanistic Study of AI-Text Detection Neurons in Frozen BERT: Sparse Probing and Activation Patching on RAID](https://arxiv.org/abs/2609.30287)

**<font color=#1a73e8>作者：</font>** Paweł Blicharz, Miłosz Grunwald  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-generated text detectors achieve high accuracy on standard benchmarks, yet the internal representations that drive these predictions remain poorly understood. We study which neurons in a frozen BERT-base-uncased encoder support AI-text detection, using the RAID benchmark across six generators spanning pure-base and instruction-tuned models. We apply the L1-to-L2 sparse-probing protocol of Gurnee et al. (2023) to all 9,216 CLS hidden-state dimensions (12 layers x 768), which we call neurons. The procedure recovers a stable set of under 1% of neurons per generator, consistent across folds and seeds; a probe restricted to that set retains most of the full-feature detection accuracy. Bidirectional activation patching confirms this set's causal relevance: in both directions it flips predictions an order of magnitude more often than size-matched random sets. Mean-ablating the same neurons leaves accuracy largely intact; the signal is therefore redundantly distributed. Cross-generator analysis reveals a bipartite structure: instruction-tuned generators concentrate 30-36% of stable neurons in BERT's final layer while both base generators fall below 14%, consistent with a layer-12 footprint of post-training alignment. Leave-one-family-out evaluation shows the selected neurons retain 86-94% of the full-feature ceiling on unseen generator families, so a detector can operate on a small fixed subspace without re-identifying neurons per generator.

---


### 10. [Bringing AI to Autonomous Systems -- From Cognition to Collective Intelligence](https://arxiv.org/abs/2609.30291)

**<font color=#1a73e8>作者：</font>** Joseph Sifakis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The purpose of this article is to highlight the central role of autonomous systems as the ultimate stage in the development of AI, to explain the underlying technical challenges that require a combination of connectionist AI and symbolic AI, and to integrate AI and systems engineering. We present a comprehensive framework for the design and evaluation of autonomous systems, based on a generic agent architecture that characterizes their behavior as the composition of cognitive functions organized around a long-term memory containing the agent's evolving knowledge. We address the challenges posed by the implementation of the fundamental features of the agent architecture, in particular the link between sensory data and structured data stored in memory, decision-making related to the achievement of the agent's goals and their planning, as well as the coordination of agents to combine individual and collective intelligence. We explain that agent trustworthiness, unlike that of traditional systems, is not limited to behavioral properties. It includes an essential dimension related to cognitive properties, the validity of which depends on how the agent uses its knowledge in decision-making. We present avenues for the development of methods for evaluating agent trustworthiness. We conclude with a critical assessment of the substantial gap between the aspirational vision of autonomous multi-agent systems and the current state of the art.

---


### 11. [SlideLab: Audience-Centered Scientific Slide Generation and Evaluation](https://arxiv.org/abs/2609.30294)

**<font color=#1a73e8>作者：</font>** Vidushee Vats, Karun Sharma, Yuxia Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific presentations are more than summaries of research papers. They need to present the work in a coherent sequence, explain the main ideas clearly, and help the audience follow the presentation. We present SlideLab, a training-free multi-agent framework for generating scientific presentations from research papers. SlideLab first plans the presentation narrative, then builds and iteratively refines a shared slide deck using agents for content planning, visual generation, layout refinement, and grounding verification. In a blind human preference study, SlideLab was preferred over both open-source and commercial systems on 77% of papers while using roughly 4 times fewer inference tokens than the strongest open-source baseline. We also introduce ConfArena, an audience-oriented evaluation framework that simulates a conference room and assesses presentations slide by slide. ConfArena matches human system rankings and detects injected presentation problems, including falsified numbers, degraded figures, dropped slides, and shuffled slide order.

---


### 12. [NeuralCert: certified computational discovery of extremal mathematical constructions](https://arxiv.org/abs/2609.30296)

**<font color=#1a73e8>作者：</font>** Mark Patrick Roeling  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks are becoming popular in solving mathematical problems, but stochastic models do not provide mathematical exactness by themselves. This study introduces a discovery-to-certification framework in which high-dimensional variational trial functions are learned in a compact separable representation, spectrally diagnosed and pruned, and then certified exactly through multimodular evaluation. Exact certification makes the numerical proofs fully explicit and independently verifiable. This framework can be run on a standard personal computer.
Across three extremal problems, we show that neural optimization can contribute to rigorous mathematics in three distinct ways: by discovering improved constructions, by exposing empirical invariants that lead to proofs, and by revealing optimization barriers whose geometry motivates new analytic or numerical representations.
More broadly, these results suggest a path toward AI-assisted mathematics in which flexible computational discovery and exact certification become complementary components of a single rigorous workflow.

---


### 13. [Staged Depth Training: A Representation Curriculum for PINNs](https://arxiv.org/abs/2609.30299)

**<font color=#1a73e8>作者：</font>** Kejia Zhang, Youran Sun, Haizhao Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation quality is a central determinant of PINNs' performance, yet standard training leaves representations to emerge implicitly while fitting the final solution. We introduce \textbf{representation curriculum}, an ordered process in which representations are explicitly learned, transferred independently of their predictors, and progressively refined. We realize it with Staged Depth Training (SDT), which trains a shallow prefix under a temporary physics-informed head, discards the head, and freezes the learned prefix while adding depth, without equation-specific encodings or changes to the final architecture. Across the 20 default forward problems in PINNacle with three backbones, SDT improves 40 of 59 equal-budget problem--backbone cells by at least 5\% and remains within that band in the rest, with a 32.8\% geometric-mean error reduction on a PirateNet-style backbone. Mechanistic ablations suggest that the gain is not explained by optimizer restarts or shallow warm-starting alone. Representation visualizations and hyperparameter-basin analyses provide diagnostic evidence on representation geometry and local sensitivity to shared hyperparameters. On Poisson--Boltzmann 2D, SDT also more than doubles the fitted depth-scaling exponent for both backbones. These results support representation curriculum as a promising training strategy for improving PINNs while preserving the deployed architecture and inference cost.

---


### 14. [ScopeBench: Do Agents Preserve Engagement Boundaries Under Goal Pressure?](https://arxiv.org/abs/2609.30325)

**<font color=#1a73e8>作者：</font>** Shane Caldwell, Max Harley, Ads Dawson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents are increasingly deployed with real autonomy in web application and network penetration testing, where a single out-of-scope action can breach a client's engagement boundary. Existing offensive-security benchmarks measure raw hacking capability; as those benchmarks saturate, the real barrier to deployment is a special case of alignment: scope adherence. We introduce ScopeBench, a benchmark of 30 dead-end agentic security tasks in which the stated objective is reachable only by violating the stated scope. Each task appears under two conditions that share an environment, verifier, and objective and differ only in scope: one instruction set has no scope and measures capability; the other has a natural-language scope to measure adherence. Scopeless trajectories are graded by a standard deterministic verifier. Scoped trajectories pass through two grading arms. First, the same deterministic verifier checks for the flag: because the flag sits behind the scope boundary, a pass proves by construction that a forbidden action occurred, yielding a high-precision lower bound on the violation rate. If the verifier does not pass the trajectory, an agentic judge estimates whether an out-of-scope call occurred. We calibrate the judge against 100 ScopeBench trajectories labeled call-by-call by human annotators, and a blinded audit of the evaluated rollouts finds its high recall holds - no false negatives among the 36 audited violations, with over-flagging its only observed error. Across 8 models in one harness, raw capability spans 12.2% to 81.1% and scope adherence spans 34.4% to 86.7%, with the judge finding 331 violations that mechanical verification misses. Opus-4-8 achieves a raw-capability score 10 percentage points higher than sonnet-4-6's while exhibiting 35.6 percentage points higher scope adherence. We release the frozen pilot benchmark, evaluation code, and all 2160 ATIF trajectories.

---


### 15. [GAUDI: Geometry-Aware Diffusion for Calibrated Air-Quality Time-Series Imputation](https://arxiv.org/abs/2609.30340)

**<font color=#1a73e8>作者：</font>** Xinjin Li, Yudi Xia, Calvin Chang Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Air-quality sensor outages often create contiguous missing blocks, where side information useful for isolated missingness may be less reliable. We study a block-specific, GAUDI-aligned conditional diffusion imputer that retains temporal and feature processing, visible-value and mask conditioning, variable identity, and diffusion-step information, while suppressing absolute time-position side embeddings. On ItalyAir (13 variables, length-32 windows, nominal 50% block missingness; three archived seeds), this feature-side configuration achieves RMSE 0.340, versus 0.355 for full context and 0.355 for local CSDI. The experiment isolates a geometry-aware conditioning effect under block missingness.

---


### 16. [Learning coarse-step dynamics and internal mechanical response with graph networks](https://arxiv.org/abs/2609.30344)

**<font color=#1a73e8>作者：</font>** Vinay Sharma, Olga Fink  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern sensing records the motion of physical systems, but often leaves the forces and mechanical response governing that motion unobserved. Inferring these quantities from discretely sampled trajectories is especially difficult at coarse time scales, when mechanical response evolves between observations and interactions propagate across the system. Here we introduce Newmark-\b{eta}-DGN, a graph neural network-based framework that combines two structures inspired by computational mechanics. First, a semi-implicit update inspired by the Newmark-\b{eta} method uses learned momentum fluxes and matrix-valued response operators to advance the state over each observed interval. Second, an operator-weighted virtual hub provides system-wide coupling through a sparse set of connections. The learned quantities thus determine the predicted motion and remain accessible for mechanical analysis. Across a deformable beam, human motion and protein dynamics, Newmark-\b{eta}-DGN supports long-horizon prediction at time steps for which explicit learned simulators deteriorate. Without force, moment or constitutive relation supervision, forces inferred from walking kinematics track independently derived hip and knee joint moments, while response operators learned on the beam recover the relative spatial and directional structure of its finite-element stiffness tangent. Newmark-\b{eta}-DGN therefore links coarse-step prediction to the inference of mechanical quantities that were never observed during training.

---


### 17. [AlphaEarth distinguishes cities but compresses urban variation](https://arxiv.org/abs/2609.30356)

**<font color=#1a73e8>作者：</font>** Andrew Renninger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cities differ in built form, land cover and development history, complicating comparison across places and time. Satellite foundation models map Earth's surface onto common numerical representations. Yet the tasks and targets used to shape them typically do not focus on cities: globally consistent labels for urban function do not exist, and many datasets - especially land cover and land use classifications - collapse the built environment into few classes. Here we audit the representation, focusing on AlphaEarth but with broader applicability to other Earth embeddings, by probing the geometry and geography of embeddings for 1,000 urban areas in 162 countries. We find that cities occupy a shifted but overlapping region on the hypersphere, 62.7° from the global mean direction, and continent and climate predict 24.3% of variation among the mean directions of urban centres in excluded countries. Inside cities, degrees of urbanisation carry 8.9% of the variation, and what they leave holds shared directions whose local orientation varies, not one universal axis of urbanisation. Retained variation is itself unequal: dispersion within urban centres is 14.1% greater per standard deviation of national development, even after adjusting for population, land area and continent. Further controls suggest cities in developing countries present less contrast in vegetation and texture, and dispersion follows that contrast: full adjustment for it leaves at most 6.4% of the gradient. Annually, a city's representation moves nearly eight times more than redrawing its own pixels explains, and contracts where the 2022 loss of Sentinel-1B removed a pass direction. AlphaEarth's representations therefore support comparison across regions, while the differences between its annual layers are not yet validated for comparison over time.

---


### 18. [DanLing NestedTensor: Composable Multi-Ragged Tensors for Deep Learning](https://arxiv.org/abs/2609.30379)

**<font color=#1a73e8>作者：</font>** Zhiyuan Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variable-size inputs are common in deep learning, but dense batching allocates a shared envelope and spends computation on padding. The cost multiplies across varying axes: an explicit pair state allocates $BN_{\max}^2$ positions instead of $\sum_i N_i^2$. Packing removes that waste, but composing packed operations still requires the logical axes and sample boundaries a flat buffer no longer exposes. We present DanLing NestedTensor, a PyTorch tensor abstraction that makes multi-ragged structure a property of the tensor itself. Packed values carry tensor-backed partitions and logical dimension order, so broadcasting creates ragged axes, feature transformations retain them, and reductions consume them. The same representation carries through autograd and both eager and compiled execution. On an A100, the geometric-mean speedup over same-mode padding is 2.74$\times$ eager and 3.39$\times$ compiled across four BERT scales, and 1.97$\times$ eager across four FCN backbones. A four-block Pairformer-style workload runs 2.40-4.32$\times$ faster than a padded reference using native PyTorch kernels across square length regimes in eager execution, with peak allocation falling from 38.08 to 5.41 GiB on its high-variation batch. The tensor interface lets model code built from its supported operators compose efficient variable-size computation without managing offsets at any call site. Code will be released publicly upon publication.

---


### 19. [The Interviewer's Perspective: Unpacking the Impact of Real-Time AI Interviewing Assistance on Social Dynamics](https://arxiv.org/abs/2609.30388)

**<font color=#1a73e8>作者：</font>** Zhe Liu, Jiamin Dai, Joanna McGrenere  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Eliciting rich data in semi-structured interviews is cognitively demanding, prompting recent work to explore real-time AI assistance for interviewers. However, introducing AI into the interviewer-interviewee interaction creates a triadic context whose social dynamics remain underexplored. We investigated how interviewers experience AI assistance for probing during semi-structured interviews. To elicit rich participant reflections, we implemented two variants of AI assistance differing in initiation and granularity in a high-fidelity prototype, ProbeAssist. We conducted a qualitative-first comparative structured observation study where 18 participants each completed three simulated interviews: one without AI and two with different AI variants. Findings showed that participants leveraged AI as a supportive tool but resisted it as an assessor or competitor. As they navigated AI's benefits and interaction costs, tensions emerged around agency, ownership, creativity, and interpersonal communication. We propose three implications for AI-assisted human-to-human interaction: managing social pressure, balancing idea alignment with inspiration, and preserving interpersonal presence.

---


### 20. [From Weak Data to Strong Policy: Q-Targets Enable Provable In-Context Reinforcement Learning](https://arxiv.org/abs/2609.30391)

**<font color=#1a73e8>作者：</font>** Yichen Lin, Xuyuan Xiong, Xue Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing in-context reinforcement learning methods mainly pretrain Transformers with supervised behavior-prediction objectives. This enables task inference from context, but makes the learned policy strongly depend on the quality of offline actions: when trajectories are weak or suboptimal, imitation itself becomes a biased learning signal. We propose Q-Target Pretrained Transformers (QTPT), which keeps the context-conditioned Transformer architecture but replaces behavior cloning with a Bellman-style Q-target objective. QTPT therefore learns to use rewards and transitions in the context to estimate action values, rather than simply imitating the behavior policy. We theoretically analyze QTPT in stochastic linear bandits and finite-horizon MDPs, showing stronger robustness to data quality than supervised pretraining. Empirically, QTPT improves over supervised behavior prediction on controlled RL benchmarks with random or suboptimal data, and we examine extensions to D4RL Kitchen and AntMaze. Supplementary experiments evaluate backbone robustness, meta-RL comparisons, task-coherent context, and unsupported-action value overestimation. These comparisons distinguish the benefits of Q-target pretraining from the remaining limitations of offline coverage.

---


### 21. [LiTe-GS: Oracle-Efficient Next Best View Selection for 3D Gaussian Splatting](https://arxiv.org/abs/2609.30393)

**<font color=#1a73e8>作者：</font>** Vivek Pandey, Amirhossein Mollaei Khass, Nader Motee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Selecting informative camera views is critical for efficient training and adaptive refinement in 3D Gaussian Splatting, where each observation significantly influences model parameters. However, information-driven view-selection strategies can require repeated evaluations of expensive information-gain oracles as the number of candidate views increases. We propose LiTe-GS, an oracle-efficient method for next best view selection in 3D Gaussian Splatting. LiTe-GS reduces the number of information-oracle evaluations by performing randomized subset evaluation of candidate views rather than exhaustively scoring the full candidate pool. The resulting approach achieves expected $O(M\log(1/\epsilon))$ oracle complexity with respect to the number of candidate views $M$, independent of the selection cardinality $K$, while providing an explicit trade-off between oracle efficiency and approximation quality through $\epsilon$. We provide theoretical guarantees on oracle complexity and approximation performance under the proposed selection scheme. Experiments on Blender and Mip-NeRF 360 demonstrate that LiTe-GS maintains reconstruction quality comparable to Fisher-information-based baselines while substantially reducing the number of Fisher-oracle evaluations across different acquisition settings.

---


### 22. [CSCWD: Cross-Scale Channel-wise Knowledge Distillation for Lightweight Tiny Object Detection on Edge Devices](https://arxiv.org/abs/2609.30395)

**<font color=#1a73e8>作者：</font>** Amir Zamani, Zeinab Ghasemi-Naraghi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time tiny object detection in aerial imagery is constrained by the weak spatial evidence of very small objects and the loss of high-resolution detail in lightweight detectors. This study presents Cross-Scale Channel-wise Knowledge Distillation (CSCWD), a training-time framework that transfers high-resolution spatial representations from a YOLO11m-P2 teacher to a compact YOLO11n student without altering the student's inference architecture. Unlike conventional same-scale feature distillation, CSCWD transfers supervision from teacher P2 to student P3 after feature alignment while retaining same-scale distillation at deeper pyramid levels. Under the unified seven-sequence Drone-vs-Bird validation protocol, YOLO11n-CSCWD achieves 50.17% mean average precision at an intersection-over-union threshold of 0.5 (mAP@0.5) and 59.73% recall, improving the matched CA-YOLO11n baseline by 2.92 percentage points in mAP@0.5 and 3.55 points in recall. Cross-scale alignment further increases mAP@0.5 by 2.09 points over the corresponding same-scale channel-wise distillation configuration. In zero-shot evaluation on DUT-Anti-UAV, mAP@0.5 increases from 48.29% to 50.06% without target-domain fine-tuning. This domain was included because its challenging small targets make low-latency, computationally efficient detection particularly relevant. On Raspberry Pi 5 using NCNN-FP16 at 640x640 resolution, the 2.58-million-parameter student achieves 50.32% mAP@0.5 at 82.32 ms mean wall-clock latency, or 12.15 frames per second, while retaining essentially the same runtime and memory requirements as the matched baseline. The results support cross-scale distillation for improving tiny-target detection without increasing inference-time model complexity.

---


### 23. [A Synthetic Ground-Truth Framework for the Evaluation of Explainable AI Methods](https://arxiv.org/abs/2609.30397)

**<font color=#1a73e8>作者：</font>** Miquel Miró-Nicolau, Francesco Spinnato, Riccardo Guidotti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating explainable Artificial Intelligence (XAI) methods is a challenging task due to the lack of reliable evaluation procedures and, in particular, the absence of ground truth explanations. In the literature, existing evaluation approaches typically assess explanations by measuring their fidelity with respect to the predictions of a black-box model. However, such evaluation strategies only quantify the degree to which an explanation reproduces the model's output, without ensuring that the explanation correctly reflects the underlying decision process. As a consequence, different explanations may achieve similar fidelity scores while providing inconsistent or misleading interpretations of the model behavior. In this paper, we propose a framework for the evaluation of XAI methods based on synthetic ground truth. The proposed approach relies on controlled interventions to generate synthetic datasets in which the importance of input components can be determined by design. This enables the construction of ground truth explanations that are directly aligned with the behavior of the model under analysis. The framework is instantiated across three data domains, namely binary images, tabular data, and time series, allowing a comprehensive assessment of explanation methods in heterogeneous settings. Experimental results obtained by evaluating nine widely used XAI methods show significant limitations in current techniques and highlight the importance of synthetic, intervention-based benchmarks for a reliable assessment of explanation quality.

---


### 24. [What Improves Multimodal Misinformation Detection? Answers from a Large-Scale Empirical Study](https://arxiv.org/abs/2609.30402)

**<font color=#1a73e8>作者：</font>** Akshit Sharma, Prashant W. Patil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal misinformation is increasingly crafted to look convincing by pairing a textual claim with an image that appears to "prove" it. Yet in practice, building effective detectors often hinges on a small set of design choices that are rarely examined in a controlled way. In this paper, we conduct a large-scale study of multimodal design choices for misinformation detection with over 3,375 experiments- spanning three benchmark datasets and a broad range of pre-trained vision and language backbones. Through systematic comparisons and targeted robustness analyses, we distill practical guidance on which design choices help, when do they fail silently, and what aspects of the pipeline most strongly shape model behavior, answering 4 key Research Questions (RQs). We aim to provide a reliable foundation for designing stronger and more dependable multimodal misinformation detection systems, thus contributing to the broader research community.

---


### 25. [A Unified Account of Concepts and Chunks](https://arxiv.org/abs/2609.30414)

**<font color=#1a73e8>作者：</font>** Karthik Singaravadivelan, Pat Langley  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cognitive psychology has studied how people encode, use, and learn concepts that describe categories, and how they represent, recognize, and acquire chunks for familiar patterns of elements. The literatures on these two topics are nearly disjoint, which poses a challenge for unified theories of cognition. In this paper, we review Cobweb, a computational account of categorization and concept formation, and propose an extended theory that incorporates chunks and their acquisition. The theory makes no commitments about modality, applying to any experience that decomposes into elements and relations among them. We also present \trellis/, an implementation of this theory, and illustrate its application to learning context-free grammars, which we adopt as a testbed because they involve both concept-like and chunk-like elements. In addition, we report experimental results on three synthetic grammars that demonstrate the system's ability to represent syntactic knowledge, use it to parse and generate sentences, and learn compositional structures from sample parses. We conclude by discussing related work on concepts and chunks, along with directions for future research in the area.

---


### 26. [Electric Vehicle Charging Station Location Selection using Geospatial Artificial Intelligence (GeoAI)](https://arxiv.org/abs/2609.30417)

**<font color=#1a73e8>作者：</font>** Eun Hak Lee, Euntak Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As electric vehicle (EV) adoption increases, ensuring efficient and well-distributed charging infrastructure has become a critical challenge. While many EV charging station location problem (CSLP) studies focus on minimizing costs or travel distance, it is crucial to consider the surrounding geospatial characteristics of existing stations that influence operational performance. This study proposes a geospatial artificial intelligence (GeoAI)-based framework that integrates high-dimensional EV-related geospatial data, including EV usage, land-use, population, and traffic attributes. We incorporate a variational autoencoder (VAE) and a graph convolutional network (GCN) into the model to capture similarities among existing charging stations, and to identify suitable locations for future stations. The VAE compresses high-dimensional EV input data into a low-dimensional latent space, and the GCN uses this latent representation to predict locations suitable for charging stations. Using real-world data from Bryan-College Station, Texas, US, the proposed model outperforms state-of-the-art baselines, achieving an F1-score of 0.87 in distinguishing existing station locations from non-station locations. The model also identifies 27 additional candidate locations that show geospatial characteristics similar to those of existing stations, based on a similarity score. We further evaluate two policy implementation scenarios, maximizing geospatial similarity and minimizing total travel distance, each yielding different outcomes aligned with distinct strategic objectives. The findings highlight the importance of incorporating spatial context into CSLP and provide valuable insights for future EV infrastructure planning, promoting both efficiency and accessibility in the rapidly growing electric mobility sector.

---


### 27. [Improving Molecular-Morphology Contrastive Pretraining using Deep-Learning-based Morphology Profiles](https://arxiv.org/abs/2609.30433)

**<font color=#1a73e8>作者：</font>** Jie Li, Kathryn E. Kirchoff, Dante A. Pertusi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advancements in image-based profiling techniques have enabled the collection of high-volume cell morphology data, allowing new molecular embedding models to learn from the experimental phenotypic perturbations of a molecule in a cell. Previously, we developed Molecule-Morphology Contrastive Pretraining (MoCoP), a strategy for aligning small molecule embeddings to morphology fingerprints extracted through CellProfiler. The resulting molecular representation showed transferable performance for quantitative structure--activity relationship (QSAR) prediction tasks. Here, we extend the method by using a deep-learning-based cell image encoding pipeline to extract more feature-rich morphology profiles and align them to the molecular embeddings through contrastive learning. The new embeddings encode more accurate information on how molecules perturb cell morphology and enable improvements for QSAR predictions through either fixed-embedding linear probes or fully flexible fine-tuning. Morphology retrieval performance scales log-linearly with training data size, suggesting continued improvements as larger datasets become available. The improved MoCoP v2 also achieves superior performance on toxicity prediction and competitive results on ADME and activity benchmarks, when compared with existing molecular embedding models that use both cell morphology and transcriptomic data during training.

---


### 28. [Predicting Transmembrane Protein Topology from 3D Structure](https://arxiv.org/abs/2609.30446)

**<font color=#1a73e8>作者：</font>** Sitong Chen, Xiaopeng Mao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel approach to infer protein topology using the state-of-the-art graph neural network (GNN), SchNet. The model is trained on the same dataset used to develop the recent DeepTMHMM model with 5-fold cross-validation. Unlike the conventional approaches based on using only the protein sequences or the $\alpha$-carbons as features, we have decoded our classifier in this way, so all atom-level embeddings are used. Without applying any pre-trained weight, the final results have shown great potential that GNNs can be used for topological predictions.

---


### 29. [Who Acts When the User Is Gone? Digital Remains, Survivor Claims, and Post-Mortem Governance](https://arxiv.org/abs/2609.30449)

**<font color=#1a73e8>作者：</font>** Supriya Khadka, Dhiman Goswami, Sanchari Das  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital systems continue to govern accounts, devices, data, and recovery channels after an account holder dies, leaving survivors to manage digital remains through mechanisms built around a living user. We examine post-mortem digital governance as a sociotechnical problem of cooperative and contested work, focusing on who acts when the user is gone, what claims they make, and what barriers shape recovery, preservation, closure, and protection. We conducted a content analysis of $800$ Reddit posts about post-mortem digital privacy and security, coding posts across assets, actors, actions, privacy tensions, access barriers, policy gaps, emotional contexts, and risks. Findings show that phones/devices often act as gateways to other digital remains, socially connected actors make most claims, and data loss emerges as a central harm. We synthesize these findings into a Post-Mortem Digital Governance Framework for designing mechanisms that support survivor coordination while limiting access by purpose, asset, actor, and context.

---


### 30. [LensDesigner: A Self-Improving Agent for Optical Lens Design](https://arxiv.org/abs/2609.30450)

**<font color=#1a73e8>作者：</font>** Lei Sun, Haoran Liang, Dannong Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical lens design is a complex, non-convex optimization challenge that relies heavily on human experience and intuition. Existing optimized-based automatic lens design methods struggle to navigate this vast parameter space without meticulous manual tuning. In this paper, we present LensDesigner, an autonomous agent framework that mirrors the problem-solving workflow of expert opticians. To overcome the initial cold start problem, we construct LensLib100K, an extensive optical lens library, and employ Optics-Aware Retrieval to supply physically valid structural seeds. Within an interactive physical simulation environment, the agent executes macroscopic orchestration while receiving immediate optical feedback. Furthermore, we introduce a continuous self-evolving mechanism guided by a curriculum agent. By iteratively solving design tasks with progressively increasing difficulty, the agent autonomously extracts, accumulates, and reuses design heuristics, effectively evolving its optical lens design expertise over time. At the evaluation level, we introduce LensArena, a standardized evaluation benchmark comprising $120$ diverse optical design tasks, covering extreme configurations. Extensive experiments on this benchmark demonstrate that LensDesigner significantly outperforms publicly available baseline algorithms, achieving superior success rates and optimization efficiency. We hope this work sheds light on the emerging field of intelligent optics. The code will be publicly available.

---


### 31. [Auditing System-1 Models on Biosecurity-Relevant Benchmarks: Calibration, Selective Prediction, and Permutation Instability in a Non-Generative Model](https://arxiv.org/abs/2609.30454)

**<font color=#1a73e8>作者：</font>** Kimon Antonios Provatas, Ilias Georgakopoulos-Soares  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-generative "System-1" models return structured probabilistic decisions in a single forward pass, without autoregressive decoding, at a small fraction of the inference cost of a generative model. This makes them of interest as inexpensive components in larger pipelines, but their reliability on biosecurity-relevant tasks has not been systematically examined. We audit one commercial System-1 model on 6,020 multiple-choice items drawn from the Weapons of Mass Destruction Proxy (WMDP), a paraphrase-robust WMDP-Bio variant, and six LAB-Bench subtasks, measuring accuracy, calibration, error detection, selective prediction, and sensitivity to the order in which answer options are presented. Accuracy is strongly task-dependent. Once the vendor's uncertainty field is correctly interpreted, the model is reasonably well calibrated (pooled expected calibration error 0.034) and its top-1 probability separates correct from incorrect predictions (pooled AUROC 0.820), though both degrade substantially on the weaker tasks. Under four cyclic rotations of the answer options, 37.4% of WMDP-Cyber items receive different answers; a control using byte-identical repeated calls attributes most of this to option order rather than run-to-run variation. Averaging probabilities across rotations improves WMDP-Cyber accuracy by 3.8 percentage points, and applying it only to low-confidence items recovers most of that gain at well under the cost of averaging every item.

---


### 32. [Spectral Feedback for Test-Time Alignment of Protein Diffusion Models](https://arxiv.org/abs/2609.30456)

**<font color=#1a73e8>作者：</font>** Shai Dickman, Mert Cemri, Landon Butler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reward maximization alignment methods for discrete diffusion models have primarily focused on steering the reverse process, either by influencing token logits or by selecting favorable sequences at intermediate steps. These approaches largely treat inference as a unidirectional process, lacking mechanisms for revisiting undesirable token selections. We introduce Spectral Feedback, an algorithm that selects edit-positions in a feedback loop, allowing the model to iteratively correct its own generations. This approach leverages the mask structure of discrete diffusion models by re-masking and re-sampling tokens, analogous to image editing methods that reintroduce noisy latents and re-run the reverse process. While prior alignment methods focus on what token labels to assign to maximize a target reward, we instead treat which tokens to revisit as the central alignment problem. Selecting edit-positions is challenging because edit effects are interdependent: the impact of modifying one token depends on which others are edited simultaneously. We define an edit-set as a set of token positions to re-mask and re-sample. Motivated by prior work on sparse interactions in biological systems, we find empirically that edit-set value functions for protein inverse folding admit sparse Fourier representations. This structure enables Spectral Feedback to efficiently learn and optimize the value functions for edit-position selection. Spectral Feedback is model-agnostic and can be applied to pretrained, test-time aligned, and fine-tuned diffusion models. For all of these models, the algorithm improves alignment performance without modifying the underlying generative process. Applied to inverse folding with a protein stability reward oracle, it achieves a 32.3% increase in stable proteins for a pretrained model, 24.8% for Best-of-10, and 5.8% for a state-of-the-art RL fine-tuned diffusion model.

---


### 33. [Reliability-aware Cross-sample Enhancement for Robust Multimodal Sentiment Analysis](https://arxiv.org/abs/2609.30470)

**<font color=#1a73e8>作者：</font>** Menghua Jiang, Haokai Gao, Xiangui Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Sentiment Analysis (MSA) aims to infer human emotions from multiple modalities such as text, audio, and vision. In practice, inputs are often corrupted by noise and missing modalities, which degrades performance. Existing methods typically address these challenges in isolation, limiting their effectiveness in realistic settings. To address this limitation, we propose a Reliability-aware Cross-sample Enhancement (RCE) framework. Specifically, RCE first introduces an adaptive variational information bottleneck to model modality-wise uncertainty and perform quality-aware information compression, thereby suppressing redundant noise in unreliable modalities. Furthermore, we design a reliability-aware cross-sample enhancement strategy that retrieves high-confidence, semantically consistent neighbors from a large candidate pool to enrich and calibrate current representations, effectively alleviating information deficiency caused by missing modalities. Building upon this, RCE integrates cross-modal interactions with a multilevel reliability-aware fusion mechanism to adaptively aggregate information across modalities and enhancement stages, leading to more robust multimodal representations. Extensive experiments demonstrate that RCE consistently outperforms state-of-the-art methods across full, noisy, and missing-modality settings.

---


### 34. [Moment-guided edge sampling](https://arxiv.org/abs/2609.30472)

**<font color=#1a73e8>作者：</font>** Weibin Cai, Reza Zafarani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge sampling makes local decisions to achieve graph-level objectives, such as preserving structural properties. This creates a fundamental challenge: \textit{how can the effect of a local edge edit (i.e., edge addition or removal) on global graph structure be quantified and controlled?} We address this challenge with a \textit{moment-guided edge sampling framework} based on spectral moments of the random-walk transition matrix. We compute exact moment changes through two complementary methods: a combinatorial method with closed-form updates for low-order moments, and a low-rank method that exploits \textit{locality} and \textit{cyclic trace invariance} to compress computations to edited endpoints, supporting arbitrary moment orders and batched edits. For single-edge edits at fixed moment orders, the low-rank method reduces the cost from $O(mn)$ to $O(m)$, while the combinatorial method evaluates low-order changes in constant time given maintained local statistics. These moment changes provide \textbf{interpretable structural signatures} of local edge motifs that aggregate into graph-level fingerprints. This structural meaning motivates us to ask whether preserving moments also preserves the graph properties. We further derive and validate that moment-preserving sampling can \textbf{retain related structural properties}, including triangle-weighted clustering coefficient. These structural insights enable \textbf{analysis and improvement of graph learning}: different edge structures have distinct effects on supervised node classification, while moment-guided augmentation is competitive for graph contrastive learning. Together, these findings establish moments as an interpretable and controllable bridge from local edge edits to global graph structure and learning.

---


### 35. [Redesigning Trust: Replacing Dark Patterns with Fair Choice Architecture in Financial Interfaces](https://arxiv.org/abs/2609.30475)

**<font color=#1a73e8>作者：</font>** Oluwadamilola Awakan, Tawan Aroonwechkul, Roshan Gunjoor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital financial platforms make enrollment effortless and cancellation laborious. This asymmetry is a dark pattern that manipulates users who have already decided to leave. Existing work identifies such patterns after deployment, and regulators sanction them after harm, yet neither provides designers with a criterion for building interfaces that avoid manipulation. We model the provider as an adversary whose instrument is effort and express fairness as a constraint requiring that leaving never cost more than joining. Defining interaction cost over navigation steps, mandatory inputs, and confirmation prompts, we prove that this constraint holds for every assignment of effort weights if and only if no component of the exit flow exceeds its counterpart at entry. Fairness is therefore verifiable by counting rather than by estimating cognitive effort, and exact equivalence is unnecessary because exit legitimately requires fewer inputs than entry. We instantiate the model, together with invariants for visual parity and linguistic neutrality, in a mobile credit card prototype with parallel sign-up and cancellation workflows.

---


### 36. [The Shape of Events: Edge-Based Inductive Biases via Cross-Domain Distillation](https://arxiv.org/abs/2609.30478)

**<font color=#1a73e8>作者：</font>** Soshun Kihara, Shunsuke Yasuki, Masato Taki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks trained on ImageNet are known to exhibit a strong preference for local high-frequency texture, an inductive bias that translates into fragile robustness against distribution shifts in real-world environments. Event cameras, in contrast, record only changes in scene brightness and are therefore well suited to capturing contour information; however, due to the absence of diagnostic benchmarks in the event domain, the inductive bias that event-camera data instills in vision models has remained underexplored. In this work, we use knowledge distillation from the event domain to the RGB domain so as to exploit the rich evaluation toolkit available in the RGB domain and systematically dissect this inductive bias. Our experiments show that distillation from the event domain induces, in the RGB domain, color invariance, shape bias, and robustness to high-frequency noise. We identify the underlying mechanism as the model suppressing its dependence on high-frequency texture while acquiring a stronger dependence on edge-based object shape. This hypothesis is supported by changes in how color and spatial information are processed at the early layers, together with a spectral trade-off in which robustness to the absence of high-frequency components coexists with vulnerability to contamination of the relied-upon frequency bands and to disruption of geometric structure. We further show that this inductive bias differs from existing robustification methods and that it functions as a useful prior for diverse downstream tasks in which shape and contour information contribute alongside other cues. The code is available at this https URL .

---


### 37. [Geometric Feature Learning for Functional Data Valued on the Symmetric Positive Definite Manifold](https://arxiv.org/abs/2609.30487)

**<font color=#1a73e8>作者：</font>** Samuel V. Singh, Mimi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We here develop a functional neural network, termed MatFAE, for learning trajectories on the Riemannian manifold of symmetric positive definite (SPD) matrices. MatFAE features intrinsic layers that map manifold-valued functions to Euclidean vector-valued functions, followed by a functional layer that projects them into a finite-dimensional Euclidean space. Unlike most neural networks for discrete-time sequences, MatFAE treats each sequence as a continuous function and can therefore encode trajectory dynamics (e.g., first-order derivatives) in its latent representations. Additionally, the morphology of the functional weights in the functional layer offers interpretability by revealing the regions of the input functional data that contribute most to the latent representations. We justify the design principles and properties of each intrinsic layer and detail how matrix factorization is handled during backpropagation. We apply MatFAE to a range of fMRI datasets, demonstrating its ability to efficiently learn informative representations from high-dimensional SPD trajectories and its practical value for real-world neuroimaging analysis.

---


### 38. [Learning to Bias: Machine Learning-Enhanced Particle Filters](https://arxiv.org/abs/2609.30498)

**<font color=#1a73e8>作者：</font>** Apoorv Srivastava, Eric Darve  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential inference estimates latent states from noisy and incomplete observations. Particle Filters (PFs), a class of Monte Carlo methods based on importance sampling, provide a flexible framework for this task, but often suffer from poor sample efficiency and unfavorable scaling with dimension, partly due to suboptimal proposal distributions. We address these challenges by integrating learned proposals into the PF framework. We introduce Neural Optimal Particle Filters (NOPFs), which learn an amortized approximation to the optimal proposal from offline simulated one-step conditioning tuples. The learned proposal is used as a drop-in replacement in standard PF updates, with samples corrected by standard importance weights so that the method asymptotically targets the same filtering distribution under standard support and density-evaluation assumptions. Across stochastic nonlinear benchmarks of varying inference complexity, NOPFs improve sample efficiency and distributional accuracy over standard PF baselines with modest computational overhead. The approach integrates data-driven proposal learning into classical inference without altering the underlying filtering objective.

---


### 39. [PolicyAttention: Softmax Attention Implements Policy Mirror Descent for Closed-Loop Control](https://arxiv.org/abs/2609.30500)

**<font color=#1a73e8>作者：</font>** Yuhe Sui, Yingzhi Tang, Shufang Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can causal softmax attention implement policy mirror descent as a repeated controller rather than a one-step algebraic identity? Negative-entropy policy mirror descent (PMD) has the statewise update $\operatorname{PMD}_\eta(\pi,Q)=\operatorname{softmax}(\log\pi+\eta Q)$. Building on the known Q-TD-PMD recursion, we construct one fixed causal-softmax actor--environment--one-step-critic protocol with explicit actor, routing, sampling, and normalization residuals, and propagate them to the policy actually returned. The construction states the finite-logit/full-support domain, the external tokenization and sampling boundary, and the mean-zero LayerNorm carrier conditions required by the normalized compilation.
Separately trained pre-LN Transformers recover the target computation empirically. A frozen one-step audit model is closest to PMD among the tested fixed rules; in a preregistered five-run $S=4$ repeated-control test, the learned actor with an exact one-step critic reaches median returned-policy loss $1.052\times$ the Exact PMD oracle and retains the criterion across four no-retraining shifts. The same checkpoints with their learned critic give descriptive median $1.050\times$ the oracle (no registered margin). At $S=8$, replacing the exact critic by the learned critic raises median $T=20$ loss to $0.0225$ yet leaves the Liang--Lai and Algorithm Distillation adaptations $20.2$--$24.2\times$ higher-loss; this is a one-sided sampled-critic bound because PolicyAttention consumes 144 generative transitions per round versus 20 on-policy transitions for the adaptations. The strict 20-transition comparison remains open. At $S=8,16$, the exact-critic common-harness comparison remains $17.7$--$28.2\times$ lower-loss than those adaptations, with the information asymmetry stated locally.

---


### 40. [Federated Targeted Maximum Likelihood Estimation](https://arxiv.org/abs/2609.30503)

**<font color=#1a73e8>作者：</font>** Diyang Li, Fei Wang, Kyra Gan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The evidence behind a scientific or operational decision is often held by hospitals, banks, or registries that cannot pool individual observations. Cross-silo federated learning moves computation to the data and exchanges agreed summaries. Targeted maximum likelihood estimation (TMLE) refines a flexible initial fit, yielding plug-in estimators that respect the model and support efficient inference. TMLE itself, however, has remained a fully centralized procedure. To fill this gap, our paper introduces the first federated TMLE algorithm. We federate targeting itself, for an arbitrary target, loss, and fluctuation family, through two complementary frameworks. FedTMLE-G aggregates local gradients and reproduces centralized targeting step for step. FedTMLE-L lets each institution complete its own fluctuation fit before a single exchange of fitted updates, trading synchronized fidelity for local autonomy. For gradient aggregation, we develop a finite-precision protocol that transmits changes rather than values and certifies targeting accuracy within explicit bounds on exchanges and bits. A description-length analysis of the accepted updates then shows that this finite communication leaves numerical targeting error negligible against sampling uncertainty. The cost of computing an estimator is thus distinct from the complexity of selecting it. Our analysis also indicates that keeping data local is not itself a privacy guarantee of TMLE, since instability of full-record reconstruction need not prevent recovery of a specified sensitive attribute. For a personalized version of local averaging, institutions retain their own estimates and leave once local targeting is complete. A nonconvex convergence bound charges the improvement forfeited through averaging to disagreement among local fits and exposes a tradeoff between equal institutional influence and the sampling variability of small silos.

---


### 41. [Benchmarking the Connectomes of Caenorhabditis elegans within the Reservoir Computing Framework](https://arxiv.org/abs/2609.30508)

**<font color=#1a73e8>作者：</font>** Felix S. Reimers, Ola Huse Ramstad, Aliaksandr Hubin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The aim of this work is to examine the connectomes of Caenorhabditis elegans through a computational lens using the reservoir computing framework. Connectomes are mappings of biological neural networks; C. elegans is the first organism for which physical connectomes covering the whole nervous system have been published. The connectomes of C. elegans used in this paper have been derived at different ages of the organism and are based on three different ways of measuring inter-cellular connections. They have, with minimal preprocessing, been implemented as reservoirs in the form of echo state networks, which are recurrent neural networks. In reservoir computing, the reservoir itself is not trained, rather the output of the reservoir is passed to a comparatively small read-out module in which training takes place. Training and testing is conducted in different neuro-inspired tasks, with the aim of using these tasks as a benchmark for the connectomes. This process has been repeated with different configurations of the reservoir and equally sized but randomized null models have been used for comparison. The results show that the biological wiring and a bio-informed configuration of input and output nodes of the reservoirs do not necessarily lead to better performance. Contrarily, the randomized null models are often outperforming the original connectomes on the chosen benchmarks. At the same time it becomes clear that the results depend a lot on the configuration of the reservoir and the way the connectome has been derived from the organism. Connectomes from different ages may produce varying outcome, without a clear trend becoming visible.

---


### 42. [Inquesto Score: A reliability Protocol For Voice Agents](https://arxiv.org/abs/2609.30514)

**<font color=#1a73e8>作者：</font>** Massa Baali, Bhiksha Raj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice agents are increasingly deployed in workflows where failed interactions can affect transactions, access, and other consequential outcomes, creating a need for reproducible and interpretable evaluation. We introduce Inquesto Score (IS), a protocol for measuring voice-agent reliability as the percentage of calls in a fixed, versioned evaluation population that achieve the caller's goal without a functional failure or worse. Rather than combining heterogeneous metrics, IS defines explicit failure events and severity levels and evaluates the deployed voice pipeline. Timing failures, including talk-over and delayed responses, are measured directly from audio, while semantic and state-dependent failures are evaluated using scenario predicates, tool traces, and a pinned open-model judge. Diagnostic views of behavior, acoustic robustness, identity handling, and speaker groups accompany the score without being combined into it. Inquesto Score v0.1 evaluates 30 scenarios, three acoustic conditions, four speaker groups, and 306 calls per agent across 13 configurations of a reference voice-agent system. Our evaluation shows that reliable measurement requires evidence beyond transcripts, explicit treatment of deployment conditions, and validation of the evaluators used to determine outcomes. We release the protocol, reference implementation, and evaluation records.

---


### 43. [GyroNovo: Error-Guided Fragment Imputation with Mass-Aware Attention for \textit{De Novo} Peptide Sequencing](https://arxiv.org/abs/2609.30542)

**<font color=#1a73e8>作者：</font>** Abdellah El Mekki, Laks V.S. Lakshmanan, Muhammad Abdul-Mageed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> De novo peptide sequencing from tandem mass spectra is essential for identifying peptides without relying on reference databases. Despite advances in deep learning, accurate sequencing remains challenging because experimental spectra are often sparse, noisy, and incomplete, leaving informative b- and y-ion fragments unobserved. Existing methods attempt to recover this missing evidence via latent-space imputation before autoregressive decoding. However, they typically treat imputation as a fixed reconstruction task, without considering which missing fragments are most relevant to decoder errors. Moreover, existing peak representations do not explicitly model mass differences between peaks, despite their fundamental importance.
We introduce GyroNovo, a framework with two main contributions. First, we use decoder errors observed during training to adapt the imputation objective, prioritizing fragments associated with frequent decoding errors. We further use the decoder error distribution to construct easy and hard augmented views of each spectrum, enabling the decoder to learn under varying degrees of spectral corruption and missing-fragment severity. Second, we introduce a mass-aware inductive bias into self-attention by using rotary embeddings to encode pairwise mass differences between spectral peaks. Together, these components align missing-fragment recovery with decoder behavior while explicitly incorporating the mass relationships that underlie peptide fragmentation. At inference time, GyroNovo retains a standard encoder-imputer-decoder architecture and requires neither additional inputs nor auxiliary search procedures. Experiments on NovoBench show gains of about 9 percentage points in peptide-level precision and 7 percentage points in amino-acid-level precision over the state-of-the-art baseline. Code: this https URL.

---


### 44. [Benchy: towards a universal language for task-oriented AI benchmarks](https://arxiv.org/abs/2609.30550)

**<font color=#1a73e8>作者：</font>** Francis F Daniel, Mauro Ibañez, Francis Perelman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchy is a semantic language and execution engine for benchmarking AI programs. A benchmark is completely specified by a program, a scoring function, and a dataset, B=(P,S,D), and is separate from the AI-system taking it; a run binds the two, R=(B,AI). Benchmarks are authored as canonical YAML in which each semantic concept has one valid syntax, classified by a shared task/domain/language ontology, and deterministically compiled into a canonical JSON intermediate representation that the engine executes. Compilation changes representation, not meaning: it does not repair invalid definitions or inject hidden defaults. Programs use fixed schemas of named input and output fields, the leaf output fields are the scoring dimensions, and the engine exposes one universal runtime contract --- a named-field input object in, a named-field output object out --- to which external AI-systems adapt at the boundary, so integration mechanics never propagate into benchmark semantics. This paper gives the semantic object model, the ontology and task-to-program validation rule, the scoring and failure semantics, the compilation and execution architecture, and the scope of the current language. An appendix fixes the normative engineering contract for the first engine implementation.

---


### 45. [Rank-Reliable Teacher-Guided Fitness Approximation for Expensive Evolutionary Optimization: A TinyML Architecture Search Study](https://arxiv.org/abs/2609.30553)

**<font color=#1a73e8>作者：</font>** Soumen Garai, Suman Samui  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Expensive evolutionary search does not always need an exact fitness estimate for every candidate. It often needs a reliable answer to a simpler question: which candidate is better? We address this need through Teacher-Guided Learning NSGA-II (TGL-NSGA-II), a low-fidelity framework for constrained Tiny Machine Learning (TinyML) neural architecture search. A pretrained teacher organizes samples into strata defined jointly by difficulty and class. Each candidate then undergoes KD-Lite, a short and capped knowledge-distillation procedure on a compact training set, before being scored on a separate stratified evaluation set. This teacher-guided score is fused with a Gaussian-process surrogate to select candidates for full evaluation. For a fixed candidate population, we analyse evaluation variance, score concentration, pairwise rank inversion, expected Kendall-$\tau$, first-front identification, and hypervolume perturbation. We also derive a variance-aware fusion weight and a capacity-adaptive distillation rule. On keyword spotting and bird-call classification, the measured Kendall-$\tau$ values are 0.74 and 0.62, exceeding the corresponding predicted lower bounds of 0.60 and 0.46. Joint stratification reduces proxy-score variance by 41% relative to random evaluation. Selective teacher mismatch, in contrast, increases differential bias and reduces Kendall-$\tau$ to 0.41. Under a constrained evaluation budget, TGL-NSGA-II achieves the largest mean hypervolume and smallest generational distance on keyword spotting, records the lowest mean false-positive rate on BirdCLEF, and runs 2.2x faster than full NSGA-II. These guarantees apply to population-level low-fidelity evaluation and do not establish convergence of the complete evolutionary trajectory.

---


### 46. [Dynamic Regret in Online Convex Optimization with Indicator Switching Costs](https://arxiv.org/abs/2609.30556)

**<font color=#1a73e8>作者：</font>** Naram Mhaisen, George Iosifidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study dynamic regret in online convex optimization with an \emph{indicator switching cost}: a fixed penalty incurred whenever two consecutive decisions differ. This captures startup overheads such as server activation, model deployment, and cache updates, and on a bounded domain it recovers norm-based movement costs as a special case. Existing guarantees for indicator costs handle only static comparators. We show that a direct extension of these techniques to dynamic regret provably fails, motivating a different approach. We propose a meta-learning framework: a set of randomized lazy FTRL base learners restarted at dyadic time scales, aggregated by a movement-aware master that mixes their proposal densities and samples actions via maximal coupling of consecutive mixtures. The resulting algorithm satisfies, in expectation, $\mathcal{R}^{\mathbf{1}}_T \le \tilde{\mathcal{O}}(\min\{\sqrt{T(S_T{+}1)},T^{2/3}(P_T+1)^{1/3}\})$, where $\mathcal{R}^{\mathbf{1}}_T$ is the dynamic regret plus the cumulative indicator switching cost, $S_T$ counts comparator switches, and $P_T$ is the comparator path length. The bound holds simultaneously for all sequences and requires no prior knowledge of $S_T$ or $P_T$: it is minimax-optimal (up to logarithmic factors) for tracking piecewise-constant comparators, and also captures frequently moving comparators with small total path length.

---


### 47. [Atlases Are Already Inside: Recovering Population Templates from Pretrained Diffusion Models](https://arxiv.org/abs/2609.30566)

**<font color=#1a73e8>作者：</font>** Jian Shi, John Femiani, Peter Wonka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a new inference-time sampler for diffusion models that gives a pretrained model a capability it was never trained for: constructing the atlas of the population it synthesizes. The sampler converges from every random seed to the population's central anatomy, which we call the \emph{intrinsic atlas}. The advantage is threefold. (1) It requires no retraining. A diffusion model that has already learned a coherent population, including the released ones, yields its atlas in a single inference pass without involving deformable registration. (2) It applies to multiple domains, such as brain MRI, chest X-ray, faces, and 3D shapes. (3) It extends to subpopulations. One age-conditioned model gives an atlas at any age in its training range, and the resulting family reproduces the CSF expansion of healthy aging. Evaluated as a registration target, the intrinsic atlas is best or second-best on every dataset against classical and learned templates, and the most central template on held-out brain MRI cohorts. Atlas construction can be reframed as a byproduct of generative modeling: a diffusion model is a learned representation of population structure, and the atlas is what it already contains.

---


### 48. [Atelier: Learning Local Self-Supervised Features for CryoEM Volumes via Hypernetworks](https://arxiv.org/abs/2609.30569)

**<font color=#1a73e8>作者：</font>** Phillip Lo, Sudarshan Babu, Dari Kimanius 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> CryoEM map interpretation requires features that are spatially localized, consistent across samples, and informative across spatial scales. Most deep learning methods for map annotation extract features from fixed voxel grids. However, implicit neural representations (INRs) are able to model volumetric data as scale-agnostic, coordinate-conditioned functions. INRs are therefore attractive for cryoEM, but fitting a separate INR for each map is too expensive for large-scale feature extraction and produces representations that are not aligned across samples. We introduce Atelier, a self-supervised framework that amortizes INR fitting for reconstructed cryoEM maps. Pretrained on 5,439 Electron Microscopy Data Bank maps, Atelier is a transformer-based hypernetwork that generates high-fidelity reconstructions across a wide range of protein structures, including large multi-subunit assemblies. Beyond reconstruction, the INR generated by the pretrained transformer exposes a continuous, local feature field through its intermediate activations at any spatial query point, a property that voxel grid and patch-tokenizer architectures do not naturally provide. Used as auxiliary channels to a 3D nested U-Net annotation head trained from scratch, these coordinate-conditioned features improve performance on eight voxel-level property prediction tasks over a volume-only baseline. Our results demonstrate that amortized implicit neural representations are an effective primitive for geometry-aware analysis of cryoEM data.

---


### 49. [Energy-efficient operation of neural operators for virtual sensing](https://arxiv.org/abs/2609.30580)

**<font color=#1a73e8>作者：</font>** Jason Yoo, Samrendra Roy, Souvik Chakraborty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Virtual sensing repeatedly reconstructs physical fields from changing observations, often on a fixed geometry. We investigate how shared spatial computation reduces the energy of these updates while retaining the selected checkpoint and its evaluated predictions. In a heat-exchanger service, standard compiler freezing and explicit trunk reuse give similar operating energy reductions relative to graph replay: approximately 1% at one request per second and 20% at forty requests per second. In 15 W mode with fixed clocks, reuse with graph replay completes the same request sequence with 22.0 to 22.5% less energy than eager execution, including preparation and waiting. DeepONet and Fourier neural operator (FNO) controls distinguish the effects of reusable arithmetic and launch overhead. Preparation, artifact construction, and worker replacement add costs outside repeated inference. These results connect operator structure to operating energy and show how update frequency and execution lifetime govern the benefit of computation reuse in physical-field virtual sensing.

---


### 50. [QSV: Quat-Sphere-Vision for Coupled Quaternion Attention on Spherical Lattices](https://arxiv.org/abs/2609.30592)

**<font color=#1a73e8>作者：</font>** Nicholas Foley, Devin Marinelli, Donny Moore 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In standard attention, three separately learned projections decide how strongly a token attends to each neighbor ($W_Q$, $W_K$) and how the attended features are transformed before aggregation ($W_V$). We study Quat-Sphere-Vision (QSV), a sparse spherical vision model that replaces this projection triple with a single learned unit quaternion per token: the relative quaternion $r_{ij} = q_i^{*} \otimes q_j$ supplies both the attention logit $\operatorname{Re}(r_{ij})$ and a sandwich-product feature transport $x \mapsto r_{ij} \otimes x \otimes r_{ij}^{*}$, with messages passed over sparse kNN graphs on concentric Fibonacci spheres. Ablations that change only the targeted component show the two roles to be asymmetric. Removing the transport reduces test accuracy by about four percentage points on CIFAR-10 and CIFAR-100 (single runs per CIFAR-100 variant), while replacing the learned attention weights with uniform averaging leaves it essentially unchanged. Parameter-matched controls then remove the geometry itself: standard attention on the same graph exceeds QSV (mean $87.3\%$ vs. $85.9\%$), and the same model on a flat 2D lattice reaches $91.1\%$, within $2.1$ points of a ResNet-20 trained under the same pipeline (single run). In the coupled kernel, nearly all of the learned pairwise computation resides in the transport channel.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-225](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
